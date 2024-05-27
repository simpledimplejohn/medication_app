# medication_app/views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import MedicationEvent

def log_medication(request, medication_name, dosage):
    if request.method == "POST":
        MedicationEvent.objects.create(
            medication_name=medication_name,
            dosage=dosage,
            timestamp=timezone.now()
        )
        return redirect('medication_app:home')
    return redirect('medication_app:home')

def home(request):
    return render(request, 'medication_app/home.html')
