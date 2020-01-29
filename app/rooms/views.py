from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404
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
    context = {
        "city": request.GET.get("city").capitalize(),
    }
    return render(request, "rooms/search.html", context)