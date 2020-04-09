from mock import patch

from ..utils import get_tokens_for_user
from .factories import (UserFactory)

from django.test import Client
from rest_framework import status
from abc import ABC
import json
import uuid


class BaseTestCase(ABC):
	@classmethod
	def setUpTestData(cls):
		cls.client = Client()
		cls.user = UserFactory()
		cls.auth_token = get_tokens_for_user(cls.user)
		cls.auth = f'Bearer {cls.auth_token["access"]}'

		cls.serializer = None
		cls.url = None
		cls.qs = None


	def test_list_200(self):
		serializer = self.serializer(self.qs, many=True)
		response = self.client.get(
				self.url,
				HTTP_AUTHORIZATION=self.auth
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, serializer.data)


	def test_retrieve_200(self):
		item = self.qs.first()
		serializer = self.serializer(item)

		response = self.client.get(
				self.url + f'{item.id}/',
				HTTP_AUTHORIZATION=self.auth
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, serializer.data)

	def test_retrieve_404_invalid_uuid_in_url(self):
		response = self.client.get(
				self.url + 'fake-id/',
				HTTP_AUTHORIZATION=self.auth
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_retrieve_404(self):
		pk = str(uuid.uuid1())
		response = self.client.get(
				self.url + f'{pk}/',
				HTTP_AUTHORIZATION=self.auth
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_update_400(self):
		item = self.qs.first()
		data = json.dumps(dict())

		response = self.client.patch(
				self.url + f'{item.id}/',
				HTTP_AUTHORIZATION=self.auth,
				content_type='application/json',
				data=data
		)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_update_404(self):
		pk = str(uuid.uuid1())
		response = self.client.patch(
				self.url + f'{pk}/',
				HTTP_AUTHORIZATION=self.auth,
				content_type='application/json',
				data=json.dumps({'table': 'New name'})
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_create_400(self):
		data = json.dumps(dict(
				name=str(uuid.uuid1()),
				is_ready=str(uuid.uuid1())
		))
		response = self.client.post(
				self.url,
				HTTP_AUTHORIZATION=self.auth,
				content_type='application/json',
				data=data
		)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_destroy_204(self):
		item = self.qs.first()
		response = self.client.delete(
				self.url + f'{item.id}/',
				HTTP_AUTHORIZATION=self.auth,
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_destroy_404(self):
		pk = str(uuid.uuid1())
		response = self.client.delete(
				self.url + f'{pk}/',
				HTTP_AUTHORIZATION=self.auth
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
