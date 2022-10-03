from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Place(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    direction = models.CharField(max_length = 50)
    phoneNumberRegex = RegexValidator(regex = r"^\+?57?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, null=True, blank=True)
    opening_hours = models.CharField(max_length = 50)
    visit_date = models.DateField(null=True, blank=True)
    logo = models.ImageField(upload_to='media/places/logo', blank=True)
    photo = models.ImageField(upload_to='media/places/photo', blank=True)

    def __str__(self):
        return self.name