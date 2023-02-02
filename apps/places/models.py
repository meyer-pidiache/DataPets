from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Place(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    direction = models.CharField(max_length = 50)
    visit_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='media/places/photo', blank=True)

    def __str__(self):
        return self.name