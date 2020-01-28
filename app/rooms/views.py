from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from . import models


def all_rooms(request):
    page = int(request.GET.get("page", 1))
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(page)
        context = {
            "page": paginator.page(page),
        }
        return render(request, "rooms/home.html", context)
    except EmptyPage:
        return redirect("/")
