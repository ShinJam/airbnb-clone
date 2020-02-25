from django.core.management import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):
    help = "This command create facilities"

    def handle(self, *args, **options):
        room_types = [
            "single",
            "double",
            "sweet",
            "king",
            "queen",
        ]
        for rt in room_types:
            RoomType.objects.create(name=rt)
        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} room types created!"))
