from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.test.client import Client
from auth.models import Users

from auth.utils import password_validation, username_validation
# Create your tests here

class TestValidators(TestCase):
    def setUp(self) -> None:
        self.valid_username = "sample_uername123"
        self.invalid_username = "sample*username"
        self.mixcase_username = "SampleName"
        self.short_username = "us"
        self.long_username = "A very very very very very very long username to fit into db"

        self.valid_password = "somepassword1234"
        self.short_password = "short"
        self.long_password = "a very very very long password to fit into database"

    def test_username(self):
        self.assertIsNone(username_validation(self.valid_username))
        self.assertRaises(ValidationError, username_validation, self.invalid_username)
        self.assertRaises(ValidationError, username_validation, self.short_username)
        self.assertRaises(ValidationError, username_validation, self.long_username)

    def test_password(self):
        self.assertIsNone(password_validation(self.valid_password))
        self.assertRaises(ValidationError, password_validation, self.short_password)
        self.assertRaises(ValidationError, password_validation, self.long_password)

class RequestTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "test_user"
        self.password = "test_password"
        self.email = "test@email.com"
        self.display_name = "test_display_name"
    
    def test_homepage(self):
        self.homepage = self.client.get('/')
        self.assertEqual(200, self.homepage.status_code)
    
    def test_new_user(self):
        print("="*40+">")
        print("Signup User Testing")
        
        #load signup page
        self.signup_page = self.client.get("/signup", follow=True)
        print(self.signup_page.redirect_chain)

        # create new user
        self.response = self.client.post("/add_user", {
            "username" : self.username,
            "password" : self.password,
            "email" : self.email,
            "display_name" : self.display_name
        }, follow=True)

        self.assertEqual(200, self.response.status_code)

        # get signup page after adding user

        self.response = self.client.get("/signup", follow=True)
        print(self.response.redirect_chain, self.response.content)
        
        self.response = self.client.get("/logout")
        self.assertEqual(302, self.response.status_code) #redirected to home page
        print("="*40+">")

