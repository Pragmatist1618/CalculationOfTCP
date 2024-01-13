# equipmentSelection/views.py
from django.http import JsonResponse
from django.shortcuts import render

from .models import Equipment


def calculate_signals(request):
    equipments = Equipment.objects.all()
    total_signals_by_type = {}

    if request.method == 'POST':
        total_signals = 0

        for equipment in equipments:
            count = int(request.POST.get(f'count_{equipment.id}', 0))
            total_signals_by_type[equipment.name] = {
                'id': equipment.id,
                'analog_input_count': count * equipment.analog_input_count,
                'analog_input_RTD_count': count * equipment.analog_input_RTD_count,
                'analog_output_count': count * equipment.analog_output_count,
                'discrete_input_count': count * equipment.discrete_input_count,
                'discrete_output_count': count * equipment.discrete_output_count,
                'pneumatic_count': count * equipment.pneumatic_count,
            }

            total_signals += sum(total_signals_by_type[equipment.name].values())

        response_data = {
            'total_signals_by_type': total_signals_by_type,
            'total_signals': total_signals,
        }

        return JsonResponse(response_data)

    context = {
        'equipments': equipments,
        'total_signals_by_type': total_signals_by_type,
        'total_signals': 0,
    }

    return render(request, 'equipmentSelection/calculate_signals.html', context)
