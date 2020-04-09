from orders.models import Order
from tables.models import Table

from django.contrib.auth import get_user_model
from django.utils import timezone
import factory
from random import randint

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class TableFactory(factory.DjangoModelFactory):
    class Meta:
        model = Table

    class Params:
        user = factory.SubFactory(UserFactory)

    created_by = factory.SelfAttribute('user')
    modified_by = factory.SelfAttribute('user')
    coordinates = (1, 1)
    size = (1, 1)
    seats = randint(1, 10)
    shape = randint(1, 2)


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = Order

    class Params:
        user = factory.SubFactory(UserFactory)
        table = factory.SubFactory(TableFactory)

    table_id = factory.SelfAttribute('table')
    created_by = factory.SelfAttribute('user')
    modified_by = factory.SelfAttribute('user')
    date = timezone.now()
