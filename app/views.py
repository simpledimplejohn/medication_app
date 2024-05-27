from django.shortcuts import render, redirect
from decouple import config
from django.http import HttpResponse

# Create your views here.
def index(request):
    SECRET_POTATO = config('SECRET_POTATO')
    print('views secret potato is: ', SECRET_POTATO)
    information = {"name":"index","secret_potato":SECRET_POTATO}
    print("information is: ",information)
    return render(request, "index.html", information)


def tomato_view(request):
    context = {}
    if request.method == 'POST':
        # Extract the data directly from POST and add it to the context
        context['tomato_name'] = request.POST.get('tomato_name', '')
        context['tomato_description'] = request.POST.get('tomato_description', '')
        context['tomato_number'] = request.POST.get('tomato_number', 0)
        context['is_tomato'] = request.POST.get('is_tomato', 'off') == 'on'
    
    return render(request, 'tomato.html', context)

