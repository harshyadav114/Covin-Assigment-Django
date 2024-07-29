from django.core.management.base import BaseCommand, CommandError
from expenses.models import User


class Command(BaseCommand):
    help = "Create Default Users"

    def handle(self, *args, **options):
        User.objects.bulk_create([User(email=f"user{i}@example.com",
              password=f"user{1}",
              name=f"user{i}",
              phone_number=f"000000000{i}") for i in range(1, 4)])
        self.stdout.write(
            self.style.SUCCESS("Successfully populated the default user"))