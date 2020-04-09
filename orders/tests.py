from orders.models import Order
from orders.serializers import OrderSerializer
from tables.tests import create_tables
from base.utils import get_tokens_for_user
from base.tests.factories import (UserFactory, TableFactory, OrderFactory)
from base.tests.tests import BaseTestCase

from rest_framework import status
from django.test import TestCase, Client
from django.utils import timezone
import json
import uuid


def create_orders(user, tables):
    orders = []
    for i in range(1, 6):
        orders.append(
            OrderFactory(user=user,
                         table=tables[i].pk,
                         name="test",
                         email="tst@tst.ts",
                         date=timezone.now()
             )
        )
    return tables


class OrderTestCase(TestCase, BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = UserFactory()
        cls.auth_token = get_tokens_for_user(cls.user)
        cls.auth = f'Bearer {cls.auth_token["access"]}'
        cls.url = '/api/orders/'
        cls.tables = create_tables(cls.user.pk)
        create_orders(user=cls.user.pk, tables=cls.tables)
        cls.qs = Order.objects.filter(created_by=cls.user.pk)
        cls.serializer = OrderSerializer
        cls._date = str(timezone.now())

    def test_create_201(self):
        data = {
            'date': self._date,
            'table': str(self.tables[0].pk),
            'name': 'user',
            'email': 'test@test.com'
        }

        response = self.client.post(
            self.url,
            HTTP_AUTHORIZATION=self.auth,
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_400_occupied(self):
        data = {
            'date': self._date,
            'table': str(self.tables[0].pk),
            'name': 'test',
            'email': 'test@test.com'
        }

        response = self.client.post(
            self.url,
            HTTP_AUTHORIZATION=self.auth,
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_400(self):
        item = self.qs.first()
        data = json.dumps(dict(table="invalid"))

        response = self.client.patch(
            self.url + f'{item.id}/',
            HTTP_AUTHORIZATION=self.auth,
            content_type='application/json',
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)