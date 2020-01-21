from django.db import models


class TimeStampdModel(models.Model):
    """ Time Stamped Model """

    created = models.DateField()
    updated = models.DateField()

    class Meta:
        abstract = True