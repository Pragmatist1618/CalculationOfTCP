# equipmentSelection/views.py

import csv

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

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

    return render(request, 'equipmentSelection/base.html', context)


def export_numbers(request):
    # Получаем словарь из параметров запроса
    params = request.GET
    # Создаем список значений из словаря
    values = list(params.values())
    # Создаем CSV-ответ
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_numbers.csv"'

    writer = csv.writer(response)
    writer.writerow(list(params.keys()))  # Заголовок
    # Пишем значения в строку CSV
    writer.writerow(values)

    return response


def import_numbers(request):
    if request.method == 'POST':
        # Assuming the CSV file is uploaded with the name 'file'
        file = request.FILES['file']

        # Decode the CSV file
        decoded_file = file.read().decode('utf-8').splitlines()

        # Get the row with two numbers (assuming there are two numbers in the file)
        values = decoded_file[1].split(',')

        # Process the numbers as needed (you may want to save them to the database)
        # For now, just print them
        # number1 = values[0]
        # number2 = values[1]
        # print("Imported values:", number1, number2)

        # Return the imported values in the JSON response
        # response_data = {
        #     'message': 'Import successful!',
        #     'importedValues': {
        #         'number1': number1,
        #         'number2': number2,
        #     },
        # }

        my_dict = dict(zip(decoded_file[0].split(','), decoded_file[1].split(',')))
        # print(my_dict)

        response_data = {
            'message': 'Import successful!',
            'importedValues': my_dict,
        }

        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'})