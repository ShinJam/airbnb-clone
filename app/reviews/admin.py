from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Review Admin Denifnition """
    list_display = ("__str__", "rating_average")
