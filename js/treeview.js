var sunburst_treeview = {
    initialize: function(){
        var sunburstWidth = $("#tree_view").width();
        var sunburstHeight = $("#tree_view").height();
        var margin = {top: 10, right: 10, bottom: 10, left: 10},
            width = sunburstWidth - margin.left - margin.right,
            height = sunburstWidth - margin.top - margin.bottom;
        var  radius = Math.min(width, height) / 2-50,
            color = d3.scale.category20c();
        var svg = d3.select("#tree_view").append("svg")
            .attr("width",width)
            .attr("height",height)
            .append("g")
            .attr("transform","translate(" + width / 2 + "," + height * 0.41 +")");
        var partition = d3.layout.partition()
            .sort(null)
            .size([2 * Math.PI, radius * radius])
            .value(function(d) {return 1;})
        var arc = d3.svg.arc()
            .startAngle(function(d) { return d.x; })
            .endAngle(function(d) { return d.x + d.dx; })
            .innerRadius(function(d) { return Math.sqrt(d.y); })
            .outerRadius(function(d) { return Math.sqrt(d.y + d.dy); });

        // read data
        d3.json("json/promotion_route.json",function(error, root){
            if(error) throw error;
            console.log(root.data[0])
            champion_name = root.data[0].name;

            var path = svg.datum(root.data[0]).selectAll(".arc_path")
                .data(partition.nodes)
                .enter().append("path")
                .attr("class","arc_path")
                .attr("d",arc)
                .style("stroke","#fff")
                .style("fill",function(d){
                    console.log(d.name)
                    console.log(d.children)
                    if(d.children || d.name == d.parent.name){
                        return color(d.name)
                    }
                    else {
                        return "lightgrey"
                    }
                    
                })
                .style("fill-rule","evenodd") 
                .on("mouseover", function(d){
                    console.log(d.name)
                    selectedpath = d3.selectAll(".arc_path")
                    selectedpath.style("opacity",function(dd){
                        if (dd.name != d.name){
                            return 0.2
                        }
                        else
                            return 1
                    })
                    
                })
                .on("mouseout", function(d){

                    selectedpath = d3.selectAll(".arc_path")
                    selectedpath.style("opacity", 1)
                                
                    
                })
                .each(stash);

            console.log(champion_name)
            var champion_text = svg.append("text")
                                    .attr("class","text")
                                    .attr("x", -margin.left*2-20)
                                    .attr("y", margin.top)
                                    .text(champion_name)
                                    .attr("font-size","20px")
                                    .attr("fill","white")

            d3.selectAll("input").on("change",function change(){
                var value = this.value === "count"? function(){return 1}:function(d){return d.size};
                path.data(partition.value(value).nodes)
                    .transition()
                    .duration(1500)
                    .attrTween("d", arcTween);
            })
        })
        function stash(d) {
            d.x0 = d.x;
            d.dx0 = d.dx;
        }
        function arcTween(a) {
            var i = d3.interpolate({x: a.x0, dx: a.dx0}, a);
            return function(t) {
                var b = i(t);
                a.x0 = b.x;
                a.dx0 = b.dx;
                return arc(b);
            };
        }

    }
}
sunburst_treeview.initialize();