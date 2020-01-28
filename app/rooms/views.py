from math import ceil

from django.core.paginator import Paginator
from django.shortcuts import render
from . import models


def all_rooms(request):
    # page = int(request.GET.get("page", 1))
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # page_count = ceil(models.Room.objects.count() / page_size)
    # context = {
    #     "potato": models.Room.objects.all()[offset:limit],
    #     "page": page,
    #     "page_count": page_count,
    #     "page_range": range(1, page_count),
    # }
    page = int(request.GET.get("page", 1))
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    context = {
        "page": paginator.page(page),
    }
    return render(request, "rooms/home.html", context)
