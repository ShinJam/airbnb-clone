from django.contrib import admin
from . import models


@admin.register(models.Room)
class RooAdmin(admin.ModelAdmin):
    pass
