from django.urls import path
from . import views
from .views import medication_app

urlpatterns = [
    path("", views.medication_app, name="index"),
]
