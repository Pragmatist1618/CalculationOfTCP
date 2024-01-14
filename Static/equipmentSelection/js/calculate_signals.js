// static/equipmentSelection/js/calculate_signals.js

$(document).ready(function () {
    var url = $("#calculation-form").data("url");

    $('input').blur(function () {
        if ($(this).val() === '') {
            // Заполняем поле значением "0"
            $(this).val('0');
        }
    });

    $("input[name^='count_']").on("input", function () {
        // Вызывать функцию обновления при каждом изменении
        calculateSignals();
    });

    //  $("#sig-reserve").on("input", function () {
    //     // Get the current value of the input
    //     let currentValue = $(this).val();
    //
    //     // Convert the value to a number
    //     let numericValue = parseFloat(currentValue);
    //
    //     // Check if the value is greater than 100
    //     if (numericValue > 100) {
    //         // If it's greater than 100, set the value to 100
    //         $(this).val(100);
    //     }
    // });
    //
    //   $("#pneu-reserve").on("input", function () {
    //     // Get the current value of the input
    //     let currentValue = $(this).val();
    //
    //     // Convert the value to a number
    //     let numericValue = parseFloat(currentValue);
    //
    //     // Check if the value is greater than 100
    //     if (numericValue > 100) {
    //         // If it's greater than 100, set the value to 100
    //         $(this).val(100);
    //     }
    // });

    function calculateSignals() {
        // Перед отправкой данных формы, установим значение 0 для пустых инпутов
        $("input[name^='count_']").each(function () {
            if ($(this).val() === "") {
                $(this).val("0");
            }
        });

        $.ajax({
            type: "POST",
            url: url,
            data: $("#calculation-form").serialize(),
            success: function (data) {
                updateTotalSignals(data);
            }
        });
    };

    function updateTotalSignals(data) {
        var totalOverallSignals = 0;
        var signalsByType = data.total_signals_by_type;

        var analogInputTotal = 0;
        var analogInputRTDTotal = 0;
        var analogOutputTotal = 0;
        var discreteInputTotal = 0;
        var discreteOutputTotal = 0;
        var pneumaticTotal = 0;

        for (var key in signalsByType) {
            var signals = signalsByType[key];
            var equipmentId = signals.id;


            $("#summ-signals-" + equipmentId + " .analog-input-1").text(signals.analog_input_count !== undefined ? signals.analog_input_count : 0);
            $("#summ-signals-" + equipmentId + " .analog-input-2").text(signals.analog_input_RTD_count !== undefined ? signals.analog_input_RTD_count : 0);
            $("#summ-signals-" + equipmentId + " .analog-output").text(signals.analog_output_count !== undefined ? signals.analog_output_count : 0);
            $("#summ-signals-" + equipmentId + " .discrete-input").text(signals.discrete_input_count !== undefined ? signals.discrete_input_count : 0);
            $("#summ-signals-" + equipmentId + " .discrete-output").text(signals.discrete_output_count !== undefined ? signals.discrete_output_count : 0);
            $("#summ-signals-" + equipmentId + " .pneumatic-output").text(signals.pneumatic_count !== undefined ? signals.pneumatic_count : 0);

            analogInputTotal += signals.analog_input_count;
            analogInputRTDTotal += signals.analog_input_RTD_count;
            analogOutputTotal += signals.analog_output_count;
            discreteInputTotal += signals.discrete_input_count;
            discreteOutputTotal += signals.discrete_output_count;
            pneumaticTotal += signals.pneumatic_count;

            var totalSignals = signals.analog_input_count + signals.analog_input_RTD_count +
                signals.analog_output_count + signals.discrete_input_count +
                signals.discrete_output_count + signals.pneumatic_count;

            $("#total-overall-signals").text(totalOverallSignals += totalSignals);
        }

        analogInputTotal += parseInt($("#count_сanalog-input-1").val(), 10);
        analogInputRTDTotal += parseInt($("#count_сanalog-input-2").val(), 10);
        analogOutputTotal += parseInt($("#count_сanalog-output").val(), 10);
        discreteInputTotal += parseInt($("#count_сdiscrete-input").val(), 10);
        discreteOutputTotal += parseInt($("#count_сdiscrete-output").val(), 10);
        pneumaticTotal += parseInt($("#count_сpneumatic-output").val(), 10);

        $("#summ-signals-type" + " .analog-input-1").text(analogInputTotal);
        $("#summ-signals-type" + " .analog-input-2").text(analogInputRTDTotal);
        $("#summ-signals-type" + " .analog-output").text(analogOutputTotal);
        $("#summ-signals-type" + " .discrete-input").text(discreteInputTotal);
        $("#summ-signals-type" + " .discrete-output").text(discreteOutputTotal);
        $("#summ-signals-type" + " .pneumatic-output").text(pneumaticTotal);

        var signalReserve = parseInt($("#sig-reserve").val(), 10);
        var pneuReserv = parseInt($("#pneu-reserve").val(), 10);

        $("#total-signals-type .analog-input-1").text(
            Math.max(0, Math.ceil(analogInputTotal + analogInputTotal * signalReserve / 100))
        );
        $("#total-signals-type .analog-input-2").text(
            Math.max(0, Math.ceil(analogInputRTDTotal + analogInputRTDTotal * signalReserve / 100))
        );
        $("#total-signals-type .analog-output").text(
            Math.max(0, Math.ceil(analogOutputTotal + analogOutputTotal * signalReserve / 100))
        );
        $("#total-signals-type .discrete-input").text(
            Math.max(0, Math.ceil(discreteInputTotal + discreteInputTotal * signalReserve / 100))
        );
        $("#total-signals-type .discrete-output").text(
            Math.max(0, Math.ceil(discreteOutputTotal + discreteOutputTotal * signalReserve / 100))
        );
        $("#total-signals-type .pneumatic-output").text(
            Math.max(0, Math.ceil(pneumaticTotal + pneumaticTotal * pneuReserv / 100))
        );
    }
});