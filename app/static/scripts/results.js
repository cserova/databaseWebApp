$(document).ready(function(){
    // Clear button
    $("#clear").click(function(){
        $("#query").val("")
        clearResults();
    });

    // Run button
    $("#run").click(function(){
        clearResults();
        if(validateForm()) {
            $.ajax({
                type: 'POST',
                url: "/results/" + $('input[name="server"]:checked').val() + "/" + $("#database").val(),
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify($("#query").val().replace('\n', ' ')),
                success: function (data) {
                    const parsed_data = JSON.parse(data);
                    if (parsed_data[0]) loadTable(parsed_data[1]);
                    else alert(parsed_data[1]);
                },
                error: function (error) {
                    alert(error);
                }
            });
        }
    });
});

function loadTable(parsed_data) {
    clearResults();
    $('#table').append('<div id="results-table"></div>');
    let results_table = new Tabulator("#results-table", {
        layout:"fitColumns",
        columns: parsed_data[0],
        pagination:"local",
        paginationSize:15,
    });
    results_table.addData(parsed_data[1]);
    $("#query_time").val("Query time: " + parsed_data[2]);
}

function clearResults() {
    $("#query_time").val("")
    $("#results-table").remove()
}

function validateForm() {
    if($('input[name="server"]:checked').val()===undefined) {
        alert("Please select a database");
        return false;
    }
    return true;
}