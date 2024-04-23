from django.shortcuts import render
import pandas as pd

def home(request):
    return render(request, 'dashboard/home.html')

def load_csv_data(request):
    file_path = '/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv'
    data = pd.read_csv(file_path)
    context = {
        'data': data.to_html(classes='table table-striped', index=False)
    }
    return render(request, 'your_template_name.html', context)
