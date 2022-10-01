from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PlaceForm

def places(request):
    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST,
                        request.FILES)
        if form.is_valid():
            form.user = request.user
            form.save()
            messages.success(request, f'¡Tu lugar ha sido agregado!')
            return redirect('places:places')
        else:
            messages.info(request, 'Información inválida')

    context = {'form': form}
    return render(request, 'places/places.html', context)