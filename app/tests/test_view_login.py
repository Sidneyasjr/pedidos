from django.test import TestCase
from django.shortcuts import resolve_url as r



class LoginTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('login'))
        self.user = self.client.post(r('login'), {'username': 'joao', 'password': '123456'})

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_template(self):
        """Must use accounts/login.html"""
        self.assertTemplateUsed(self.response, "accounts/login.html")


    def test_authentication(self):
        """POST / must return status code 200"""
        self.assertEqual(200, self.user.status_code)