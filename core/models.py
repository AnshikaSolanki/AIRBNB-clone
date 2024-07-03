from django.db import models


class TimeStampedModel(models.Model):
    """ TIME STAMPED MODEL """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

