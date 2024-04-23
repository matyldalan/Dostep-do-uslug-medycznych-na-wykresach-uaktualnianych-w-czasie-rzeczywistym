import pandas as pd

def load_csv_data(request):
    file_path = 'data/data.csv'
    data = pd.read_csv(file_path)
