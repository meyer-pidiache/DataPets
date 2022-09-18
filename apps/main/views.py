from multiprocessing import context
from django.shortcuts import render

def home(request):
    context = {'title': 'DataPets'}
    return render(request, 'main/index.html', context)

def about_1(request):
    context = {'title': '¿Qué es DataPets?'}
    return render(request, 'main/about_1.html', context)

def about_2(request):
    context = {'title': '¿Dónde encontrarnos?'}
    return render(request, 'main/about_2.html', context)

def about_3(request):
    context = {'title': 'Contáctenos'}
    return render(request, 'main/about_3.html', context)
