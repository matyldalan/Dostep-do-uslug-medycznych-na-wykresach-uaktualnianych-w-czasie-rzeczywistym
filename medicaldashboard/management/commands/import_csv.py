from django.core.management.base import BaseCommand, CommandError
from app_name.models import DataEntry
import csv

class Command(BaseCommand):
    help = 'Imports data from a specified CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv', type=str, help='/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv')

    def handle(self, *args, **options):
        file_path = options['/home/RealtimeMedicalDashboard/Dostep-do-uslug-medycznych-na-wykresach-uaktualnianych-w-czasie-rzeczywistym/medicaldashboard/data/data.csv']
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                DataEntry.objects.create(
                    value=int(row['Value']),
                    color=row['Color'],
                    letter=row['Letter']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % file_path))
