from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review

def home(request):
    reviews = list(Review.objects.order_by('-pub_date')[:6])

    context = { 'title': 'DataPets', 
                'reviews': reviews,
    }
    return render(request, 'main/index.html', context)

def about_1(request):
    context = {'title': '¿Qué es DataPets?'}
    return render(request, 'main/about/about_1.html', context)

def about_2(request):
    if request.method == 'POST':
        user = request.POST['user_name']
        messages.success(request, f'¡{user}, tu comentario ha sido guardado!')
        return redirect('main:home')

    context = {'title': '¿Dónde encontrarnos?'}
    return render(request, 'main/about/about_2.html', context)
