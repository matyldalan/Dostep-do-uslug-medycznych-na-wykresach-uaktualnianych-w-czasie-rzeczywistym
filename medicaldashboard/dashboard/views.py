from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def home(request):
    file_path = '/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv'
    data = pd.read_csv(file_path)
    letters = data['Letter'].unique().tolist()

    context = {
        'letters': letters,
        'selected_letter': None,
        'data': ''
    }

    if request.method == 'POST':
        selected_letter = request.POST.get('letter_choice')
        filtered_data = data[data['Letter'] == selected_letter]
        context['data'] = filtered_data[['ID', 'Value', 'Color']].to_html(classes='table table-striped', index=False)
        context['selected_letter'] = selected_letter

    return render(request, 'home.html', context)

def load_csv_data(request):
    if request.method == 'POST':
        selected_letter = request.POST.get('letter_choice')
        file_path = '/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv'
        data = pd.read_csv(file_path)

        filtered_data = data[data['Letter'] == selected_letter]

        context = {
            'data': filtered_data[['ID', 'Value', 'Color']].to_html(classes='table table-striped', index=False),
            'letters': list(data['Letter'].unique()),
            'selected_letter': selected_letter
        }
        return render(request, 'home.html', context)
    else:
        file_path = '/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv'
        data = pd.read_csv(file_path)
        context = {
            'data': '',
            'letters': list(data['Letter'].unique()),
            'selected_letter': None
        }
        return render(request, 'home.html', context)
