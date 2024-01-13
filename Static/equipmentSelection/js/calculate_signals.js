// static/equipmentSelection/js/calculate_signals.js

$(document).ready(function () {
    var url = $("#calculation-form").data("url");

    $("input[name^='count_']").on("input", function () {
        // Вызывать функцию обновления при каждом изменении
        calculateSignals();
    });

    function calculateSignals() {
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

            $("#total-signals-" + equipmentId + " .analog-input-1").text(signals.analog_input_count);
            $("#total-signals-" + equipmentId + " .analog-input-2").text(signals.analog_input_RTD_count);
            $("#total-signals-" + equipmentId + " .analog-output").text(signals.analog_output_count);
            $("#total-signals-" + equipmentId + " .discrete-input").text(signals.discrete_input_count);
            $("#total-signals-" + equipmentId + " .discrete-output").text(signals.discrete_output_count);
            $("#total-signals-" + equipmentId + " .pneumatic-output").text(signals.pneumatic_count);

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

        $("#total-signals-type" + " .analog-input-1").text(analogInputTotal);
        $("#total-signals-type" + " .analog-input-2").text(analogInputRTDTotal);
        $("#total-signals-type" + " .analog-output").text(analogOutputTotal);
        $("#total-signals-type" + " .discrete-input").text(discreteInputTotal);
        $("#total-signals-type" + " .discrete-output").text(discreteOutputTotal);
        $("#total-signals-type" + " .pneumatic-output").text(pneumaticTotal);
    }
});