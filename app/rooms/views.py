from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_countries import countries
from django.http import HttpResponse

from . import models


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    """ RoomDetail Definition """

    model = models.Room


def search(request):
    form = {
        "city": request.GET.get("city", "Anywhere").capitalize(),
        "s_room_type": int(request.GET.get("room_type", 0)),
        "s_country": request.GET.get("country", "KR"),
        "price": int(request.GET.get("price", 0)),
        "guests": int(request.GET.get("guests", 0)),
        "bedrooms": int(request.GET.get("bedrooms", 0)),
        "beds": int(request.GET.get("beds", 0)),
        "baths": int(request.GET.get("baths", 0)),
        "s_amenities": request.GET.getlist("amenities"),
        "s_facilities": request.GET.get("facilities"),
        "instant": request.GET.get("instant", False),
        "super_host": request.GET.get("super_host", False),
    }

    choices = {
        "countries": countries,
        "room_types": models.RoomType.objects.all(),
        "amenities": models.Amenity.objects.all(),
        "facilities": models.Facility.objects.all(),
    }
    filter_args = {}

    if form['city'] != "Anywhere":
        filter_args["city__startswith"] = form['city']

    filter_args["country"] = form['s_country']

    if form['s_room_type'] != 0:
        filter_args["room_type__pk"] = form['s_room_type']

    rooms = models.Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})
