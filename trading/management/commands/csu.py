import os

from django.contrib.auth.models import User
from django.core.management import BaseCommand



class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(username='admin', email='admin@example.com')
        user.set_password(os.getenv('SUPERUSER_PASSWORD'))
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
