# equipmentSelection/views.py

import csv

import requests
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from .models import Equipment, FSMotors, FCMotors, PLC, PLCExpansionModule, HMI, IM


def calculate_signals(request):
    equipments = Equipment.objects.all().order_by('rendering_order')
    fs_motors = FSMotors.objects.all().order_by('rendering_order')
    fc_motors = FCMotors.objects.all().order_by('rendering_order')
    plcs = PLC.objects.all()
    plc_ems = PLCExpansionModule.objects.all()
    hmis = HMI.objects.all()
    ims = IM.objects.all()

    total_signals_by_type = {}

    if request.method == 'POST':
        # total_signals = 0

        for equipment in equipments:
            count = int(request.POST.get(f'count_{equipment.id}', 0))
            total_signals_by_type[equipment.name] = {
                'etype': '',
                'id': equipment.id,
                'analog_input_count': count * equipment.analog_input_count,
                'analog_input_RTD_count': count * equipment.analog_input_RTD_count,
                'analog_output_count': count * equipment.analog_output_count,
                'discrete_input_count': count * equipment.discrete_input_count,
                'discrete_output_count': count * equipment.discrete_output_count,
                'pneumatic_count': count * equipment.pneumatic_count,
            }

            # total_signals += sum(total_signals_by_type[equipment.name].values())

        for fs_motor in fs_motors:
            count = int(request.POST.get(f'count_fs_{fs_motor.id}', 0))
            total_signals_by_type[fs_motor.name] = {
                'etype': 'fs-',
                'id': fs_motor.id,
                'analog_input_count': count * fs_motor.analog_input_count,
                'analog_input_RTD_count': count * fs_motor.analog_input_RTD_count,
                'analog_output_count': count * fs_motor.analog_output_count,
                'discrete_input_count': count * fs_motor.discrete_input_count,
                'discrete_output_count': count * fs_motor.discrete_output_count,
                'pneumatic_count': count * fs_motor.pneumatic_count,
            }

        for fc_motor in fc_motors:
            count = int(request.POST.get(f'count_fc_{fc_motor.id}', 0))
            total_signals_by_type[fc_motor.name] = {
                'etype': 'fc-',
                'id': fc_motor.id,
                'analog_input_count': count * fc_motor.analog_input_count,
                'analog_input_RTD_count': count * fc_motor.analog_input_RTD_count,
                'analog_output_count': count * fc_motor.analog_output_count,
                'discrete_input_count': count * fc_motor.discrete_input_count,
                'discrete_output_count': count * fc_motor.discrete_output_count,
                'pneumatic_count': count * fc_motor.pneumatic_count,
            }

        response_data = {
            'total_signals_by_type': total_signals_by_type,
            # 'total_signals': total_signals,
        }

        return JsonResponse(response_data)

    euro_rub = get_euro_exchange_rate('')

    context = {
        'equipments': equipments,
        'fc_motors': fc_motors,
        'fs_motors': fs_motors,
        'total_signals_by_type': total_signals_by_type,
        'euro_rub': euro_rub,
        'plcs': plcs,
        'plc_ems': plc_ems,
        'hmis': hmis,
        'ims': ims,
        # 'total_signals': 0,
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


def get_euro_exchange_rate(api_key):
    base_url = "https://open.er-api.com/v6/latest"
    params = {
        "base": "EUR",  # Используйте свою базовую валюту, если не USD
        "symbols": "RUB",
        # "apikey": api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        euro_rate = round(data["rates"]["RUB"], 2)
        # print(euro_rate)
        return euro_rate
    else:
        # Обработка ошибки, например, вывод в консоль или возвращение значения по умолчанию
        # print(f"Ошибка при получении курса: {response.status_code}")
        return None
