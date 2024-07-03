from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This Command creates Amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="how many times should i tell?")

    def handle(self, *args, **options):
        amenities = [
            "Indoor Pool",
            "Microwave",
            "Ironing Board",
            "Outdoor Pool",
            "Oven",
            "Outdoor Tennis",
            "Bathroom",
            "Queen Size Bed",
            "Shower",
            "Shoping Mall",
            "Smoke Detectors",
            "Sofa",
            "Stereo",
            "Swimming Pool",
            "Toilet",
            "Towels",
            "TV",
            "Hair Dryer",
            "Heating",
            "Golf",
            "Freezer",
            "Free Wireless Internet",
            "Fire Alarm",
            "En Suite Bathroom",
            "Free Parking",
            "Double Bed",
            "Dishwasher",
            "Cookware & Kitchen Utensils",
            "Coffee Maker in Room",
            "Cooing hob",
            "Children Area",
            "Chairs",
            "Carbon Monoxide Detectors",
            "Cable TV",
            "Boating",
            "Bathing",
            "Alarm Clock",
            "Air Conditioner",
            "Balcony",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities Created!"))

        
