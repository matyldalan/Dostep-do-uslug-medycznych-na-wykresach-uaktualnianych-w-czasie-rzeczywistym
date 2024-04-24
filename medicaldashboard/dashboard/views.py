from django.shortcuts import render
from django.core.serializers import serialize
from .models import DataEntry
import json

def home(request):
    letters = DataEntry.objects.values_list('letter', flat=True).distinct()
    selected_letter = request.GET.get('letter')
    entries = DataEntry.objects.filter(letter=selected_letter) if selected_letter else DataEntry.objects.none()
    entries_json = json.loads(serialize('json', entries))
    return render(request, 'dashboard/home.html', {
        'letters': letters,
        'entries': entries_json,
        'selected_letter': selected_letter
    })

#/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv
