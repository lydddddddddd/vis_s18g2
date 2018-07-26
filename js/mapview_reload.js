function reload_map_view() {
	map = d3.select("#map_view");

	map.selectAll(".country")
		.attr("fill-opacity", function(d) {
			if (country_state[COUNTRY_NAME.indexOf(d.properties.name)] === 1) {
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