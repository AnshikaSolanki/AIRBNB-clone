import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservations_models
from users import models as users_models
from rooms import models as rooms_models


class Command(BaseCommand):
    help = "This Command creates reservations"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="how many reservations do you want?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder.add_entity(reservations_models.Reservation, number, {
            "status": lambda x: random.choice(["pending", "canceled", "confirmed"]),
            "guest": lambda x: random.choice(users),
            "room": lambda x: random.choice(rooms),
            "check_in": lambda x: datetime.now(),
            "check_out": lambda x: datetime.now() + timedelta(days=random.randint(3,25)),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Reservations Created!"))

        
