from django.shortcuts import render
from .models import Review

def home(request):
    reviews = list(Review.objects.order_by('-pub_date')[:6])

    context = { 'title': 'DataPets', 
                'reviews': reviews,
    }
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
