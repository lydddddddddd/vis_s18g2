function load_map_view() {
	var margin = {top: 0, right: 0, bottom: 0, left: 0};
    var width = document.getElementById("map_view").clientWidth - margin.left - margin.right;
    var height = document.getElementById("map_view").clientHeight - margin.top - margin.bottom;

    var zoom = d3.behavior.zoom()
                .scaleExtent([1,5])
                .on("zoom", zoomed);

    var tool_tip = d3.tip()
                    .attr("class", "d3-tip")
                    .offset([-8, 0])
                    .html(function(d) {
                        return "<span style='color:white'>" + d.properties.name + "</span>";
                    });

    var svg = d3.select("#map_view").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .call(tool_tip);

    var svg_zoom = svg.append("g")
                    .call(zoom);

    var projection = d3.geo.mercator()
        .scale((width + 1) * 0.95 / 2 / Math.PI)
        .translate([width / 2, height * 1.42 / 2])
        .precision(.1);

    var path = d3.geo.path()
        .projection(projection); 

    var graticule = d3.geo.graticule();
 
    function zoomed() {
        $(this).attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
    }

    svg_zoom.append("path")
        .datum(graticule)
        .attr("class", "graticule")
        .attr("d", path);

    d3.json("json/world-topo-min.json", function(error, world) {
    	var countries = topojson.feature(world, world.objects.countries).features;

    	svg_zoom.append("path")
            .datum(graticule)
            .attr("class", "choropleth")
            .attr("d", path);
      
        var g = svg_zoom.append("g").call(tool_tip);
      
        g.append("path")
            .datum({type: "LineString", coordinates: [[-180, 0], [-90, 0], [0, 0], [90, 0], [180, 0]]})
            .attr("class", "equator")
            .attr("d", path);
      
        //var country = g.selectAll(".country").data(countries);
  
        //country
        g.selectAll(".country").data(countries).enter().insert("path")
                .attr("class", "country")
                .attr("d", path)
                .attr("id", function(d,i) { return d.id; })
                .attr("title", function(d) { return d.properties.name; })
                .attr("fill-opacity", "0.3")
                .style("fill", "#000099")
                // .style("fill", function(d) { return d.properties.color; })
                .on("mouseover", function(d) {
                    $(this).attr("fill-opacity", "1.0")
                    tool_tip.show(d.properties.name)
                })
                //.on("mouseover", tool_tip.show)
                .on("mouseout", function(d) {
                    $(this).attr("fill-opacity", "0.3")
                    d3.selectAll(".d3-tip").style("opacity", 0)
                    // tool_tip.hide
                })
                .on("click", function(d) {
                    console.log(d.properties.name);
                });
            
        g.append("path")
            .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
            .attr("class", "boundary")
            .attr("d", path)
            .style("fill", "none")
            .style("stroke", "#FFFFFF")
            .style("stroke-width", "1px");
    });
}