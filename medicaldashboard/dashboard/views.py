import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

def load_csv_data(request):
    file_path = 'data/data.csv'
    data = pd.read_csv(file_path)
    return HttpResponse("Data loaded successfully, number of rows: {}".format(len(data)))
    
def filter_data(request):
    selected_letter = request.GET.get('letter', '')
    data = []

    if selected_letter:
        # Ścieżka do pliku CSV
        file_path = 'data.csv'
        # Wczytanie danych z pliku CSV
        df = pd.read_csv(file_path)

        filtered_data = df[df['Letter'] == selected_letter]
        data = filtered_data.to_dict('records')

    return render(request, 'dashboard/home.html', {'data': data})
