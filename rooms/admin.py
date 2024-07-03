from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    """ITEM ADMIN DEFINITION"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()
    
    pass

class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ROOM ADMIN DEFINITION"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            'Basic Info', {'fields': ('name', 'description', 'country', 'address', 'price')},
        ),
        (
            'Times', {'fields': ('check_in', 'check_out', 'instant_book')},
        ),
        (
            'More About The Spaces', {'fields': ('amenities', 'house_rules', 'facilities')},
        ),
        (
            'Spaces', {'fields': ('bedroom', 'beds', 'guests', 'baths')},
        ),
        (
            'Last Details', {'fields': ('host',)},
        ),
   )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedroom",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    list_filter = (
        "instant_book", 
        "city",
        "country",
    )
    raw_id_fields = ("host",)
    search_fields = ("city", "^host__username")
    filter_horizontal = ("amenities", "house_rules", "facilities",)

    def count_amenities(self, obj):
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"
    

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """PHOTO ADMIN DEFINITION"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe( f'<img width="50px" src="{obj.file.url}"/>')
    
    get_thumbnail.short_description = "THUMBNAIL"
