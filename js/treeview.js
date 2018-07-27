var sunburst_treeview = {
    
    initialize: function(){
        var sunburstWidth = $("#tree_view").width();
        var sunburstHeight = $("#tree_view").height();
        var margin = {top: 10, right: 10, bottom: 10, left: 10},
            width = sunburstWidth - margin.left - margin.right,
            height = sunburstWidth - margin.top - margin.bottom;
        var  radius = Math.min(width, height) / 2-55,
            color = d3.scale.category20c();
        var svg = d3.select("#tree_view").append("svg")
            .attr("id","tree_svg")
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
        var tool_tip = d3.tip()
                    .attr("class", "d3-tip")
                    .offset([-8, 0])
                    .html(function(d) {
                        return "<span style='color:white'>" + d.properties.name + "</span>";
                    });
        svg.call(tool_tip)
        
        // read data
        d3.json("json/promotion_tree.json",function(error, root){

            if(error) throw error;

            window.global_tree_data = root; // record for update
            index = (current_year-1986)/4
            console.log(root.data[index].children)
            champion_name = root.data[index].name;
            contest_country = root.data[index].children[0].name+" vs "+ root.data[index].children[1].name;
            contest_score = root.data[index].children[0].score+" - "+root.data[index].children[1].score;
           
            var path = svg.datum(root.data[index]).selectAll(".arc_path")
                .data(partition.nodes)
                .enter().append("path")
                .attr("class","arc_path")
                .attr("d",arc)
                .style("stroke","#fff")
                //.attr("display", function(d) { return d.depth ? null : "none"; }) 
                .style("fill",function(d){
                    //console.log(d.name)
                    //console.log(d.children)
                    //console.log(d.parent)
                    if(current_country_list.indexOf(d.name) == -1){
                        current_country_list.push(d.name)
                    }
                    if(d.children || d.name == d.parent.name){
                        if(!d.parent){
                            return "white"
                        }
                        else{
                            return color(d.name)
                        }
                    }
                    else {
                        return "lightgrey"
                    }
                    
                    
                })
                .style("fill-rule","evenodd") 
                .on("mousemove", function(d){
                    /*
                    console.log(d.name)
                    selectedpath = d3.selectAll(".arc_path")
                    selectedpath.style("opacity",function(dd){
                        if (dd.name != d.name){
                            return 0.2
                        }
                        else
                            return 1
                    })
                    */
                    tool_tip.show(d.name)
                })
                .on("mouseout", function(d){

                    //selectedpath = d3.selectAll(".arc_path")
                    //selectedpath.style("opacity", 1)
                    d3.selectAll(".d3-tip").style("opacity", 0)  
                    
                })
                .on("click",function(d){
                    
                    if(!d.children || d.children.length > 2){
                        contest_country_text.text("");
                        contest_score_text.text("");
                    }
                    else{
                        contest_country = d.children[0].name+" vs "+ d.children[1].name;
                        

                        contest_score = d.children[0].score+" - "+d.children[1].score;
                        
                        contest_country_text.text(contest_country)
                                            
                        contest_score_text.text(contest_score);
                    }
                })
                .each(stash);
            console.log(current_country_list)
            console.log(champion_name)
            var contest_country_text = svg.append("text")
                                    .attr("class","contest_text")
                                    .attr("x", 0)
                                    .attr("y", -margin.top*1.5)
                                    .text(contest_country)
                                    .attr('text-anchor',"middle")
                                    .attr("font-size","14px")
                                    .attr("fill","grey")
            var contest_score_text = svg.append("text")
                                    .attr("class","contest_text")
                                    .attr("x", 0)
                                    .attr("y", margin.top*3)
                                    .text(contest_score)
                                    .attr('text-anchor',"middle")
                                    .attr("font-size","30px")
                                    .attr("fill","grey")                     
            d3.selectAll("input").on("change",function change(){
                var value = this.value === "count"? function(){return 1}:function(d){return d.size};
                path.data(partition.value(value).nodes)
                    .transition()
                    .duration(1500)
                    .attrTween("d", arcTween);
            })
            //sunburst_treeview.update_year(2018)
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

    },
    update_year:function(year){
        // 随着年份改变数据
        console.log("测试")
        console.log(window.global_tree_data)
        index = (year - 1986)/4;
        var sunburstWidth = $("#tree_view").width();
        var sunburstHeight = $("#tree_view").height();
        var margin = {top: 10, right: 10, bottom: 10, left: 10},
            width = sunburstWidth - margin.left - margin.right,
            height = sunburstWidth - margin.top - margin.bottom;
        d3.select("#tree_svg").remove();
        var  radius = Math.min(width, height) / 2-55,
            color = d3.scale.category20c();
        var svg = d3.select("#tree_view").append("svg")
            .attr("id","tree_svg")
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
        var tool_tip = d3.tip()
                    .attr("class", "d3-tip")
                    .offset([-8, 0])
                    .html(function(d) {
                        return "<span style='color:white'>" + d.properties.name + "</span>";
                    });
        svg.call(tool_tip)
        root = window.global_tree_data
        contest_country = root.data[index].children[0].name+" vs "+ root.data[index].children[1].name;
        contest_score = root.data[index].children[0].score+" - "+root.data[index].children[1].score;
           
        var path = svg.datum(root.data[index]).selectAll(".arc_path")
            .data(partition.nodes)
            .enter().append("path")
            .attr("class","arc_path")
            .attr("d",arc)
            .style("stroke","#fff")
                //.attr("display", function(d) { return d.depth ? null : "none"; }) 
            .style("fill",function(d){
                    //console.log(d.name)
                    //console.log(d.children)
                    //console.log(d.parent)
                if(current_country_list.indexOf(d.name) == -1){
                        current_country_list.push(d.name)
                }
                if(d.children || d.name == d.parent.name){
                    if(!d.parent){
                        return "white"
                    }
                    else{
                        return color(d.name)
                    }
                }
                else {
                    return "lightgrey"
                }
                    
                    
            })
            .style("fill-rule","evenodd") 
            .on("mousemove", function(d){
                   
                tool_tip.show(d.name)
            })
            .on("mouseout", function(d){                   
                d3.selectAll(".d3-tip").style("opacity", 0)                     
            })
            .on("click",function(d){
                    
                if(!d.children || d.children.length > 2){
                    contest_country_text.text("");
                    contest_score_text.text("");
                }
                else{
                    contest_country = d.children[0].name+" vs "+ d.children[1].name;
                        

                    contest_score = d.children[0].score+" - "+d.children[1].score;
                        
                    contest_country_text.text(contest_country)
                                            
                    contest_score_text.text(contest_score);
                }
            })
            .each(stash);
            
        console.log(champion_name)
        var contest_country_text = svg.append("text")
                                    .attr("class","contest_text")
                                    .attr("x", 0)
                                    .attr("y", -margin.top*1.5)
                                    .text(contest_country)
                                    .attr('text-anchor',"middle")
                                    .attr("font-size","14px")
                                    .attr("fill","grey")
        var contest_score_text = svg.append("text")
                                    .attr("class","contest_text")
                                    .attr("x", 0)
                                    .attr("y", margin.top*3)
                                    .text(contest_score)
                                    .attr('text-anchor',"middle")
                                    .attr("font-size","30px")
                                    .attr("fill","grey")                     
        d3.selectAll("input").on("change",function change(){
            var value = this.value === "count"? function(){return 1}:function(d){return d.size};
            path.data(partition.value(value).nodes)
                .transition()
                .duration(1500)
                .attrTween("d", arcTween);
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
