from django.urls import path
from .views import home, load_csv_data

urlpatterns = [
    path('', home, name='home'),
    path('load-csv/', load_csv_data, name='load-csv'),
]
