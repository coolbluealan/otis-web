from typing import Any, Dict
from typing import Union

import factory
from django.contrib.auth.models import User
from django.db import models
from django.http.response import HttpResponse
from django.test import TestCase
from django.test.client import Client
from django.urls.base import reverse_lazy


# waiting on https://github.com/FactoryBoy/factory_boy/pull/820 ...
class UniqueFaker(factory.Faker):
	# based on factory.faker.Faker.generate
	def generate(self, **params: Any) -> Any:
		locale = params.pop('locale')
		subfaker = self._get_faker(locale)
		return subfaker.unique.format(self.provider, **params)


class OTISTestCase(TestCase):
	def setUp(self):
		self.client = Client()

	def assert20X(self, response: HttpResponse):
		self.assertGreaterEqual(response.status_code, 200)
		self.assertLess(response.status_code, 300)

	def assertOK(self, response: HttpResponse):
		self.assertLess(response.status_code, 400)

	def assert40X(self, response: HttpResponse):
		self.assertGreaterEqual(response.status_code, 400)
		self.assertLess(response.status_code, 500)

	def assertDenied(self, response: HttpResponse):
		self.assertEqual(response.status_code, 403)

	def assertNotFound(self, response: HttpResponse):
		self.assertEqual(response.status_code, 404)

	def get(self, name: str, *args: Any):
		return self.client.get(reverse_lazy(name, args=args), follow=True)

	def post(self, name: str, *args: Any, data: Dict[str, Any]):
		return self.client.post(reverse_lazy(name, args=args), data=data, follow=True)

	def assertGet20X(self, name: str, *args: Any):
		self.assert20X(self.get(name, *args))

	def assertGetOK(self, name: str, *args: Any):
		self.assertOK(self.get(name, *args))

	def assertGet40X(self, name: str, *args: Any):
		self.assert40X(self.get(name, *args))

	def assertGetDenied(self, name: str, *args: Any):
		self.assertDenied(self.get(name, *args))

	def assertGetNotFound(self, name: str, *args: Any):
		self.assertNotFound(self.get(name, *args))

	def assertPost20X(self, name: str, *args: Any, data: Dict[str, Any]):
		self.assert20X(self.post(name, *args, data=data))

	def assertPostOK(self, name: str, *args: Any, data: Dict[str, Any]):
		self.assertOK(self.post(name, *args, data=data))

	def assertPost40X(self, name: str, *args: Any, data: Dict[str, Any]):
		self.assert40X(self.post(name, *args, data=data))

	def assertPostDenied(self, name: str, *args: Any, data: Dict[str, Any]):
		self.assertDenied(self.post(name, *args, data=data))

	def assertPostNotFound(self, name: str, *args: Any, data: Dict[str, Any]):
		self.assertNotFound(self.post(name, *args, data=data))

	def login_name(self, username: str):
		self.client.force_login(User.objects.get(username=username))

	def login(self, obj: Union[str, models.Model]):
		if isinstance(obj, str):
			self.client.force_login(User.objects.get(username=obj))
		elif isinstance(obj, User):
			self.client.force_login(obj)
		elif hasattr(obj, 'user'):
			self.client.force_login(getattr(obj, 'user'))

	def assertGetBecomesLoginRedirect(self, name: str, *args: Any):
		self.assertRedirects(
			self.get(name, *args), '/accounts/login/?next=' + reverse_lazy(name, args=args)
		)

	def assertPostBecomesLoginRedirect(self, name: str, *args: Any, **kwargs: Any):
		redirectURL = '/accounts/login?next=' + reverse_lazy(name, args=args)
		self.assertRedirects(self.post(name, *args, **kwargs), redirectURL)
