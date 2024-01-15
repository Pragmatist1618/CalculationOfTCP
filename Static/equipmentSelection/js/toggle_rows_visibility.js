$(document).ready(function () {
    //
    function addHideClassToZeroRows() {
        var table = $("#calculation-form");

        // Loop through each row in the table
        table.find("tbody tr").each(function () {
            var row = $(this);
            var input = row.find("input[type='number']");

            // Check if the input value is zero and the row does not have the "nohide" class
            if (input.val() === '0' && !row.hasClass("nohide")) {
                // Add the "hide" class
                row.addClass("hide");
            } else {
                // Remove the "hide" class if present
                row.removeClass("hide");
            }
        });
    }

    // Function to toggle visibility of all rows
    function toggleRowsVisibility() {
        addHideClassToZeroRows();
        var table = $("#calculation-form");
        var checkbox = $("#toggleRows");

        // Check if the checkbox is checked
        if (!checkbox.prop("checked")) {
            // If checked, show all rows
            table.find("tbody tr.hide").show();
        } else {
            // If unchecked, hide all rows
            table.find("tbody tr.hide").hide();
        }
    }

    // Initial call to set the initial state
    toggleRowsVisibility();

    // Add a change event listener to the checkbox
    $("#toggleRows").on("change", function () {
        // Call the function when the checkbox state changes
        toggleRowsVisibility();
    });
});