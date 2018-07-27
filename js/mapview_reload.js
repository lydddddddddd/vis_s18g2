function reload_map_view() {
	map = d3.select("#map_view");

	map.selectAll(".country")
		.attr("fill-opacity", function(d) {
			if (country_state[COUNTRY_NAME.indexOf(d.properties.name)] !== -1) {
				return "1.0";
			}
			else {
				return "0.5";
			}
		});

	/*map.selectAll(".boundary")
		.attr("stroke", function(d) {
			if (country_state[COUNTRY_NAME.indexOf(d.properties.name)] === 1) {
				return "IndianRed";
			}
			else {
				return "#000099";
			}
		});*/
}

function reload_map_country() {
	map = d3.select("#map_view");

	map.selectAll(".country")
		.style("fill", function(d) {
                    // console.log(current_country_list);
                    if (COUNTRY_NAME.indexOf(d.properties.name) !== -1 && current_country_list.indexOf(d.properties.name) !== -1) {
                        return "#000099";
                    }
                    else {
                        return "#DFDFDF";
                    }
                })

	reload_map_view()
}