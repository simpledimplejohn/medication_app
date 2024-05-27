# medication_app/urls.py
from django.urls import path
from . import views

app_name = 'medication_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('log/<str:medication_name>/<str:dosage>/', views.log_medication, name='log_medication'),
    path('clear/<str:medication_name>/', views.clear_history, name='clear_history'),
    path('manual_event/', views.manual_event, name='manual_event'),
]
