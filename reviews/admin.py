from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """REVIEW ADMIN DEFINITION """

    list_display = ("__str__", "rating_average")

    pass