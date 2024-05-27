# medication_app/views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import MedicationEvent
from datetime import timedelta

def log_medication(request, medication_name, dosage):
    if request.method == "POST":
        MedicationEvent.objects.create(
            medication_name=medication_name,
            dosage=dosage,
            timestamp=timezone.now()
        )
        return redirect('medication_app:home')
    return redirect('medication_app:home')

def clear_history(request, medication_name):
    MedicationEvent.objects.filter(medication_name=medication_name).delete()
    return redirect('medication_app:home')

def home(request):
    tylenol_count = MedicationEvent.objects.filter(medication_name="Tylenol").count()
    ibuprofen_count = MedicationEvent.objects.filter(medication_name="Ibuprofen").count()

    tylenol_last_event = MedicationEvent.objects.filter(medication_name="Tylenol").order_by('-timestamp').first()
    ibuprofen_last_event = MedicationEvent.objects.filter(medication_name="Ibuprofen").order_by('-timestamp').first()

    tylenol_last_timestamp = timezone.localtime(tylenol_last_event.timestamp) if tylenol_last_event else None
    ibuprofen_last_timestamp = timezone.localtime(ibuprofen_last_event.timestamp) if ibuprofen_last_event else None

    tylenol_next_dose = tylenol_last_timestamp + timedelta(hours=8) if tylenol_last_timestamp else None
    ibuprofen_next_dose = ibuprofen_last_timestamp + timedelta(hours=8) if ibuprofen_last_timestamp else None

    context = {
        'tylenol_count': tylenol_count,
        'ibuprofen_count': ibuprofen_count,
        'tylenol_last_timestamp': tylenol_last_timestamp,
        'ibuprofen_last_timestamp': ibuprofen_last_timestamp,
        'tylenol_next_dose': tylenol_next_dose,
        'ibuprofen_next_dose': ibuprofen_next_dose,
    }
    return render(request, 'medication_app/home.html', context)
