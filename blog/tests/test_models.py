from django.test import TestCase
from blog.models import MyUser



class RegistrationTestCase(TestCase):
	def setUp(TestCase):
		MyUser.objects.create(email="testase@test.com", password="test123")
		MyUser.objects.create(email="idkpieknie@gmail.com", password="admin123")

	def test_db_registration(self):
		"""if insertions to db passed, the test is ok"""
		t1_account = MyUser.objects.get(email="testase@test.com")
		t2_account = MyUser.objects.get(email="idkpieknie@gmail.com")
		self.assertEqual(t1_account.password, "test123")
		self.assertEqual(t2_account.password, "admin123")

