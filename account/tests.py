from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class RegisterTest(TestCase):
    def setUp(self) -> None:
        self.data = {
            "type": "register",
            "username": 'karim',
            "email": "",
            "phone": '09123456777',
            "password": "some123456"
        }

    def test_registerStatusCode(self):
        response = self.client.post(reverse('account:login'), data=self.data)
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'phone': '09145678238',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post(reverse('account:login'),
                                    {'type': 'login', 'username': 'testuser', 'password': 'secret'})
        # should be logged in now
        self.assertEqual(response.status_code, 302)
