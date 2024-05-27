# medication_app/views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from django import forms
from .models import MedicationEvent
from datetime import timedelta

class ManualEventForm(forms.Form):
    medication_name = forms.CharField(widget=forms.HiddenInput())
    datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label='Event Time')

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

def manual_event(request):
    if request.method == "POST":
        form = ManualEventForm(request.POST)
        if form.is_valid():
            medication_name = form.cleaned_data['medication_name']
            datetime = form.cleaned_data['datetime']
            MedicationEvent.objects.create(
                medication_name=medication_name,
                dosage="Manual Entry",
                timestamp=datetime
            )
            return redirect('medication_app:home')
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

    show_manual_form = {
        'Tylenol': tylenol_count == 0,
        'Ibuprofen': ibuprofen_count == 0,
    }

    context = {
        'tylenol_count': tylenol_count,
        'ibuprofen_count': ibuprofen_count,
        'tylenol_last_timestamp': tylenol_last_timestamp,
        'ibuprofen_last_timestamp': ibuprofen_last_timestamp,
        'tylenol_next_dose': tylenol_next_dose,
        'ibuprofen_next_dose': ibuprofen_next_dose,
        'show_manual_form': show_manual_form,
        'manual_event_form': ManualEventForm(),
    }
    return render(request, 'medication_app/home.html', context)
