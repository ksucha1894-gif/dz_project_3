from django.core.management import BaseCommand

from newuser.models import Newuser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = Newuser.objects.create(email="admin@example.com")
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
