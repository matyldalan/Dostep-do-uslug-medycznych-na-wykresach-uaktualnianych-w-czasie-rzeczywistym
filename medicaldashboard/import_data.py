import csv
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicaldashboard.settings")
django.setup()

from dashboard.models import DataEntry

def import_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            DataEntry.objects.create(
                value=int(row['Value']),
                color=row['Color'],
                letter=row['Letter']
            )

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python import_data.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    import_csv(file_path)
    print("Data imported successfully.")
