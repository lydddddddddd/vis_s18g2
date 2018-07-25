function load_map_view() {
	var margin = {top: 0, right: 0, bottom: 0, left: 0};
    var width = document.getElementById("map_view").clientWidth - margin.left - margin.right;
    var height = document.getElementById("map_view").clientHeight - margin.top - margin.bottom;

    var svg = d3.select("#map_view").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)

    var path = d3.geo.path()
        .projection(projection);

    var projection = d3.geo.mercator()
        .scale((width + 1) / 2 / Math.PI)
        .translate([width / 2, height / 2])
        .precision(.1);
      
    var graticule = d3.geo.graticule();

    svg.append("path")
        .datum(graticule)
        .attr("class", "graticule")
        .attr("d", path);

    d3.json("json/world-topo-min.json", function(error, world) {
    	var countries = topojson.feature(world, world.objects.countries).features;

    	svg.append("path")
            .datum(graticule)
            .attr("class", "choropleth")
            .attr("d", path);
      
        var g = svg.append("g");
      
        g.append("path")
            .datum({type: "LineString", coordinates: [[-180, 0], [-90, 0], [0, 0], [90, 0], [180, 0]]})
            .attr("class", "equator")
            .attr("d", path);
      
        var country = g.selectAll(".country").data(countries);
    });
}