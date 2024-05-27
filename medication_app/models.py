# medication_app/models.py
from django.db import models

class MedicationEvent(models.Model):
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication_name} - {self.dosage} at {self.timestamp}"
