from django.shortcuts import render
import pandas as pd

def home(request):
    return render(request, 'dashboard/home.html')
#/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv
