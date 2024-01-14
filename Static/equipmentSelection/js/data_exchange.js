// main.js

$(document).ready(function(){
    // Add CSRF token to all Ajax requests
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
        }
    });

    // Export button click event
    $("#export-btn").click(function(){
        var number1 = $("#number1").val();
        var number2 = $("#number2").val();

        // Redirect to export URL with parameters
        window.location.href = "/export/?number1=" + number1 + "&number2=" + number2;
    });

    // Import button click event
    $("#import-btn").click(function(){
        var fileInput = document.getElementById('import-file');
        var file = fileInput.files[0];

        // Create a FormData object and append the file
        var formData = new FormData();
        formData.append('file', file);

        $.ajax({
            url: '/import/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response){
                alert(response.message);

                // Update input values after successful import
                console.log(response)
                var importedValues = response.importedValues;
                console.log(importedValues);
                $("#number1").val(importedValues.number1);
                $("#number2").val(importedValues.number2);
            },
            error: function(error){
                alert('Import failed!');
            }
        });
    });
});
