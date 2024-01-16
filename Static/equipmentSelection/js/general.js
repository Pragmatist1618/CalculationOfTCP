$(document).ready(function () {
    var modeSelect = $('#inputEuroSelect');
    var euroRubInput = $('#euro_rub');
    var forkCheckbox = $('#checkbox-fork');
    var forkInput = $('#fork');
    var usd_rub = euroRubInput.val();


    forkCheckbox.on('change', function () {
        if (forkCheckbox.prop('checked')) {
            forkInput.prop('disabled', false);
        } else {
            forkInput.prop('disabled', true);
        }
    });

    modeSelect.on('change', function () {
        handleModeChange();
    });

    function validateInput(input) {
        // Разрешить ввод только цифр (децимальных)
        input.value = input.value.replace(/[^\d.]/g, ''); // Удаляем все, кроме цифр и точек

        // Удаляем все точки, кроме первой
        var dotIndex = input.value.indexOf('.');
        if (dotIndex !== -1) {
            var afterDot = input.value.substring(dotIndex + 1);
            input.value = input.value.substring(0, dotIndex + 1) + afterDot.replace(/\./g, '');
        }

        // Ограничиваем количество знаков после точки двумя
        var parts = input.value.split('.');
        if (parts.length > 1) {
            input.value = parts[0] + '.' + parts[1].substring(0, 2);
        }

        // Если ввод начинается с нуля, добавляем точку
        if (input.value === '0') {
            input.value += '.';
        }

        // Если поле пустое, устанавливаем значение 0
        if (input.value === '') {
            input.value = '0';
        }

        // Если после символа "0" пишется символ, добавляем точку
        if (input.value.startsWith('0') && input.value.length > 1 && input.value[1] !== '.') {
            input.value = '0' + '.' + input.value.substring(1);
        }

        // Проверяем, чтобы число было меньше 1000
        var numericValue = parseFloat(input.value);
        if (isNaN(numericValue) || numericValue >= 1000) {
            input.value = '999.99'; // Можно настроить значение по умолчанию
        }
    }

    euroRubInput.on('input', function () {
        validateInput(this);
    });

    forkInput.on('input', function () {
        validateInput(this);
    });

    function handleModeChange() {
        if (modeSelect.val() === '2') {
            euroRubInput.prop('disabled', false);
        } else {
            // Заблокировать и вернуть значение euro_rub с сервера
            euroRubInput.prop('disabled', true);
            euroRubInput.val(usd_rub);
        }
    }
});