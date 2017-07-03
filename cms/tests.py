#coding: utf-8
from django.test import TestCase
from django.contrib.auth.models import User

class HomeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/')

	def test_get(self):
		"""
		/GET must return status code 200
		"""
		self.assertEqual(200, self.resp.status_code)

class CmsTest(TestCase):
	def setUp(self):
		user = User.objects.create_user('test', 'test@a.com', 'test')
		self.client.login(username='test', password='test')
		self.resp = self.client.get('/cadastro/')

	def test_get(self):
		'GET /cadastro/ must return status code 200'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'response should be a rendered template.'
		self.assertTemplateUsed(self.resp, 'rent/cadastro_form.html')