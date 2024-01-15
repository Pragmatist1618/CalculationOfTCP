// main.js

$(document).ready(function () {
    // Add CSRF token to all Ajax requests
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
        }
    });

    // Export button click event
    $("#export-btn").click(function () {
        var inputDictionary = {};
        // Используем селектор для выбора всех инпутов внутри формы
        $('input[name^="count_"], textarea').each(function () {
            var inputName = $(this).attr('name');
            var inputValue = $(this).val();
            // Добавляем в словарь имя инпута и его значение
            inputDictionary[inputName] = inputValue;
        });
        // Выводим результат в консоль (можете использовать словарь inputDictionary по своему усмотрению)
        // console.log(inputDictionary);

        // Переменная для хранения строки параметров
        var queryParams = "";
        // Перебираем ключи и значения в объекте params
        for (var key in inputDictionary) {
            if (inputDictionary.hasOwnProperty(key)) {
                // Добавляем каждый ключ и значение к строке параметров
                queryParams += key + "=" + encodeURIComponent(inputDictionary[key]) + "&";
            }
        }
        // Убираем последний "&" из строки параметров, если он есть
        queryParams = queryParams.slice(0, -1);
        // Строим полный URL с параметрами
        var url = "/export/?" + queryParams;
        // console.log(url);

        // Redirect to export URL with parameters
        window.location.href = url;
    });

// Import button click event
    $("#import-btn").click(function () {
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
            success: function (response) {
                // alert(response.message);

                // Обновляем значения инпутов и textarea после успешного импорта
                var importedValues = response.importedValues;
                for (var key in importedValues) {
                    if (importedValues.hasOwnProperty(key)) {
                        $('input[name="' + key + '"], textarea[name="' + key + '"]').val(importedValues[key]);
                        $('input[name="' + key + '"], textarea[name="' + key + '"]').trigger('change');
                    }
                }
            },
            error: function (error) {
                alert('Import failed!');
            }
        });
    });
});
