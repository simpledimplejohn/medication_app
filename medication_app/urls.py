# medication_app/urls.py
from django.urls import path
from . import views

app_name = 'medication_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('log/<str:medication_name>/<str:dosage>/', views.log_medication, name='log_medication'),
]
