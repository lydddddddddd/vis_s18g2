var COUNTRY_NUM = 70;
var COUNTRY_NAME = new Array();
var country_state = new Array();
var country_id = new Array();
var next_country_status = 0;
var current_year = 2018;

function init_country_name() {
    country_id[0] = -1;
    country_id[1] = -1;

    d3.csv("data/team_total.csv", function(error, csvdata) {
        if (error) {
            console.log(error);
        }
        // console.log(csvdata);
        for (var i = 0; i < COUNTRY_NUM; i++) {
            COUNTRY_NAME[i] = csvdata[i].team;
            country_state[i] = -1;
            // console.log(String(i) + " " + COUNTRY_NAME[i])
        }
    })
}