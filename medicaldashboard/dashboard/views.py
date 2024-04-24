from django.shortcuts import render
from .models import DataEntry

def home(request):
    letters = DataEntry.objects.values_list('letter', flat=True).distinct()
    selected_letter = request.GET.get('letter')
    entries = DataEntry.objects.filter(letter=selected_letter) if selected_letter else DataEntry.objects.none()
    return render(request, 'dashboard/home.html', {'letters': letters, 'entries': entries, 'selected_letter': selected_letter})

#/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv
