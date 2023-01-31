from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User


class UserModelTests(TestCase):

    username = "username"
    email = "user@domain"
    password = "-insecure-"

    def test_has_many_comments(self):
        """
        has_many_comments() returns True if the user has more than 2 reviews
        """

        user = User.objects.create_user(
            username=self.username, password=self.password, email=self.email
        )

        self.assertIs(user.profile.has_many_comments(), False)
