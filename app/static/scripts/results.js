$(document).ready(function(){
    $("#query").val("select * from instacart_normalized.aisles;");

    // Clear button
    $("#clear").click(function(){
        $("#query").val("")
        clearResults();
    });

    // Run button
    $("#run").click(function(){
        $.ajax({
            type : 'POST',
            url : "/results/" + $('input[name="server"]:checked').val(),
            contentType: 'application/json;charset=UTF-8',
            data : JSON.stringify($("#query").val()),
            success: function(data) {
                const parsed_data = JSON.parse(data);
                loadTable(parsed_data);
            }
        });
    });
});

function loadTable(parsed_data) {
    clearResults();
    let columns = [];
    let column_headers = [];
    $(parsed_data[0]).each(function(index, column_name){
        columns.push(column_name);
        column_headers.push({title: column_name, field: column_name});
    });
    let results_table = new Tabulator("#results-table", {
        layout:"fitColumns",
        columns: column_headers,
        pagination:"local",
        paginationSize:15,
    });

    $(parsed_data[1]).each(function(index, row){
        const data_map = {};
        data_map["id"] = index + 1;
        $(row).each(function(index, value){
            data_map[columns[index]] = value;
        });
        results_table.addData(data_map, false);
    });

    $("#query_time").val("Query time: " + parsed_data[2]);
}

function clearResults() {
    $("#query_time").val("")
    $("#results-table").empty()
}