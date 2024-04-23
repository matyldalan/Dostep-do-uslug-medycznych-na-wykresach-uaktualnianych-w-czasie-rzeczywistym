from django.db import models

class DataEntry(models.Model):
    value = models.IntegerField()
    color = models.CharField(max_length=100)
    letter = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.letter} - {self.value} - {self.color}"
