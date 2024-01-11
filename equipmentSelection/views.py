# equipmentSelection/views.py
from django.shortcuts import render, get_object_or_404
from .models import Equipment


def calculate_signals(request):
    equipments = Equipment.objects.all()
    # total_signals_by_type = {}

    # if request.method == 'POST':
    #     total_signals = 0

    #     for equipment in equipments:
    #         count = int(request.POST.get(f'count_{equipment.id}', 0))
    #         total_signals_by_type[equipment.name] = count * (
    #                 equipment.analog_input_count +
    #                 equipment.analog_input_RTD_count +
    #                 equipment.analog_output_count +
    #                 equipment.discrete_input_count +
    #                 equipment.discrete_output_count +
    #                 equipment.pneumatic_count
    #         )
    #         total_signals += total_signals_by_type[equipment.name]
    #
    # else:
    #     total_signals = 0
    #
    # context = {
    #     'equipments': equipments,
    #     'total_signals_by_type': total_signals_by_type,
    #     'total_signals': total_signals,
    # }
    context = {
        'equipments': equipments,
    }

    return render(request, 'equipmentSelection/calculate_signals.html', context)
