from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import logging

logger = logging.getLogger('django')

def home(request):
    return render(request, 'dashboard/home.html')
#/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv

def load_csv_data(request):
    file_path = '/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv'
    data = pd.read_csv(file_path)
    letters = list(data['Letter'].unique())

    if request.method == 'POST':
        selected_letter = request.POST.get('letter_choice')
        filtered_data = data[data['Letter'] == selected_letter]
        context = {
            'data': filtered_data[['ID', 'Value', 'Color']].to_html(classes='table table-striped', index=False),
            'letters': letters,
            'selected_letter': selected_letter
        }
    else:
        context = {
            'data': '',
            'letters': letters,
            'selected_letter': None
        }

    logger.debug('Udalo sie')
    return render(request, 'home.html', context)

