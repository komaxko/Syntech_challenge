from tables.models import Table
from orders.models import Order

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from random import randint
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
        user = User.objects.filter(username='admin').first()

        # create some tables
        for i in range(1,11):
            Table.objects.create(number=i, seats=2*i, shape=randint(1,2),
                                 coordinates=[i,i], size=[i*10,i*10], created_by=user.pk, modified_by=user.pk)

        # create some orders
        date_time = datetime.strptime('2020-04-20T19:00', '%Y-%m-%dT%H:%M')
        for i in range(1, 6):
            Order.objects.create(
                table=Table.objects.filter(number=i).first(),
                date=date_time,
                name='some_name',
                email='m@il.com'
            )

        print("Tables & Orders created!")
