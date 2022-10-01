from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PlaceForm

def places(request):
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

    context = {'form': form}
    return render(request, 'places/places.html', context)