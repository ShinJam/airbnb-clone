from django.shortcuts import render
from . import models


def all_rooms(request):
    context = {
        "potato": models.Room.objects.all(),
    }
    return render(request, "rooms/home.html", context)
