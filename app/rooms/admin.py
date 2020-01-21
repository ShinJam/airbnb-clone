from django.contrib import admin
from . import models


@admin.register(models.Room)
class RooAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass
