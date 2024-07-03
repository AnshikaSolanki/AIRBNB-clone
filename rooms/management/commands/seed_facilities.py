from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This Command creates Facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="how many times should i tell?")

    def handle(self, *args, **options):
        facilities = [
            "Private Entrance",
            "Paid Parking on Premises",
            "Paid Parking off Premises",
            "Parking",
            "Elevator",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilities created!'))