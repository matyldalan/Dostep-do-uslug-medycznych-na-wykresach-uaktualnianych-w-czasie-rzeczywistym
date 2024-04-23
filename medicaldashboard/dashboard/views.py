import csv
from django.http import HttpResponse

def load_data_from_csv(request):
    path = 'data.csv'
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return HttpResponse(data)
