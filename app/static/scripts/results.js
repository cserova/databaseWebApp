let results_table = "";

$(document).ready(function(){

    //Clear button
    $("#clear").click(function(){
        let query_element = $("#query");
        if (query_element.val() === "")
            clearResults();
        else {
            if (confirm("Are you sure you want to clear the query?")) {
                query_element.val("");
                clearResults();
            }
        }
        query_element.focus();
    });

    // Shortcut for Run button
    document.addEventListener('keydown', function(event) {
        if (event.ctrlKey && event.key === '\'') {
            $("#run").click();
        }
    });

    //trigger download of data.csv file
    $("#download-csv").click(function(){
        results_table.download('csv', 'data.csv');
    });

    //trigger download of data.json file
    $("#download-json").click(function(){
        results_table.download('json', 'data.json');
    });

    // Run button
    $("#run").click(function(){
        clearResults();
        if(validateForm()) {
            $.ajax({
                type: 'POST',
                url: "/results/" + $('input[name="server"]:checked').val() + "/" + $("#database").val(),
                contentType: 'application/json;charset=UTF-8',
                data: $("#query").val().replaceAll('\n', ' '),
                success: function (data) {
                    const parsed_data = JSON.parse(data);
                    if (parsed_data[0]) loadTable(parsed_data[1]);
                    else {
                        console.log(parsed_data[1]);
                        alert(parsed_data[1]);
                    }
                },
                error: function (error) {
                    console.log(error);
                    alert(error);
                }
            });
        }
    });
});

function loadTable(parsed_data) {
    clearResults();
    $('#table').append('<div id="results-table"></div>');
    results_table = new Tabulator("#results-table", {
        layout:"fitDataFill",
        columns: parsed_data[0],
        pagination:"local",
        paginationSize:15,
        clipboard:true,
        clipboardPasteAction:"replace",
    });

    results_table.addData(parsed_data[1]);
    $("#download-controls").show()
    $("#query_time").val("Query time: " + parsed_data[2] + "   Rows returned: " + parsed_data[1].length);

}

function clearResults() {
    $("#query_time").val("");
    $("#results-table").remove();
    $("#download-controls").hide();
    $("#query").focus();
}

function validateForm() {
    if($('input[name="server"]:checked').val()===undefined) {
        alert("Please select a database");
        return false;
    }
    return true;
}