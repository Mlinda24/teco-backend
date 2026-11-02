# news/management/commands/create_superuser.py
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser if none exist'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Fetch credentials from environment variables
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write(self.style.WARNING('DJANGO_SUPERUSER_PASSWORD not set. Skipping superuser creation.'))
            return

        # Check if the user already exists
        if not User.objects.filter(username=username).exists():
            self.stdout.write(f'Creating superuser {username}...')
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully!'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} already exists.'))