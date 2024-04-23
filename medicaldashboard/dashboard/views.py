import pandas as pd
from django.http import HttpResponse

def load_csv_data(request):
    file_path = 'data/data.csv'
    data = pd.read_csv(file_path)
    return HttpResponse("Data loaded successfully, number of rows: {}".format(len(data)))
