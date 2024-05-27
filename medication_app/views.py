from django.shortcuts import render, redirect
from decouple import config
from django.http import HttpResponse

# Create your views here.
def medication_app(request):

    return render(request, "medication_app.html", {"name":"medication app"})