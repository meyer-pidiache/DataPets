from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Place
from .forms import PlaceForm

def places(request):
    places = Place.objects.order_by('-visit_date')[:18]
    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST or None,
                        request.FILES or None)
        if form.is_valid():
            place = form.save(commit = False)
            place.user = request.user
            place.save()
            form = PlaceForm()
            messages.success(request, f'¡Tu lugar ha sido agregado!')
            return redirect('places:places')
        else:
            messages.info(request, 'Información inválida')

    context = {'form': form,
               'places': places,
               'edit': False}
    return render(request, 'places/places.html', context)

def detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    context = {'place': place}
    return render(request, 'places/detail.html', context)

def edit(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    form = PlaceForm(request.POST or None, request.FILES or None, instance=place)
    if request.method == 'POST':
        form = PlaceForm(request.POST or None,
                        request.FILES or None,
                        instance=place)
        if form.is_valid():
            form.save()
            form = PlaceForm()
            messages.success(request, f'¡Tu lugar ha sido actualizado!')
            return detail(request, place_id)
        else:
            messages.info(request, 'Información inválida')

    context = {'form': form,
               'place': place,
               'edit': True}

    return render(request, 'places/edit.html', context)