from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
    """
        An external Django Command to create new User.
        To run type: python manage.py create_user
    """
    help = "Simply create a new user"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Get needed models
        User = get_user_model()

        # Get admin user
        user = User.objects.filter(username='admin')

        if not user:
            user = User.objects.create_user('admin', 'admin@domain.com',
                                            os.getenv('DJANGO_ADMIN_PASSWOD', 'password'))
            print(f'Admin created! \n')
