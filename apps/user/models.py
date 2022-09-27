from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Gender(models.Model):
    description = models.CharField(max_length = 12, null=True, blank=True)

    def __str__(self):
        return self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex = r"^\+?57?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, null=True, blank=True)
    gender = models.ManyToManyField(Gender)
    profile_picture = models.ImageField(upload_to ='static/assets/img/profiles/', null=True, blank=True)
