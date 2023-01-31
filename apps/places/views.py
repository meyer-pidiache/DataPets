from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
from .models import Place
from .forms import PlaceForm


def places(request):
    # Check if the user is authenticated to show full* content
    if request.user.id:
        places = Place.objects.order_by("-visit_date")[:21]
    else:
        places = Place.objects.order_by("-visit_date")[:3]

    context = {"places": places, "edit": False}

    return render(request, "places/places.html", context)


@method_decorator(login_required(login_url="main:home"), name="dispatch")
class Add(View):
    form = PlaceForm
    template_name = "places/add.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)  #  request.POST or None, request.FILE or None
        if form.is_valid():
            place = form.save(commit=False)
            # Author
            place.user = request.user
            place.save()
            form = PlaceForm()
            messages.success(request, f"¡Tu lugar ha sido agregado!")
            return redirect("places:places")
        else:
            messages.warning(
                request,
                "Información inválida, verifica el formato de tu número de teléfono o fecha de visita",
            )


@login_required(login_url="main:home")
def detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    context = {"place": place}
    return render(request, "places/detail.html", context)


@login_required(login_url="main:home")
def edit(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    form = PlaceForm(request.POST or None, request.FILES or None, instance=place)
    if request.method == "POST":
        form = PlaceForm(request.POST or None, request.FILES or None, instance=place)
        if form.is_valid():
            form.save()
            form = PlaceForm()
            messages.success(request, f"¡Tu lugar ha sido actualizado!")
            return detail(request, place_id)
        else:
            messages.error(request, "Información inválida")
            return detail(request, place_id)

    context = {"form": form, "place": place, "edit": True}

    return render(request, "places/edit.html", context)

# TODO Only author and admin can remove a place
def delete(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place.delete()
    messages.success(request, f"¡El lugar ha sido eliminado!")
    return redirect("places:places")
