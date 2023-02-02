from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from apps.main.models import Review

class Gender(models.Model):
    description = models.CharField(max_length = 12, null=True, blank=True)

    def __str__(self):
        return self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_editor = models.BooleanField(default=False)
    phoneNumberRegex = RegexValidator(regex = r"^\+?57?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='media/profiles/', blank=True)

    def has_many_comments(self):
        reviews = len(Review.objects.filter(user=self.user))
        if reviews < 2:
            return False
        return True

    def __str__(self):
        return f'{self.user}'