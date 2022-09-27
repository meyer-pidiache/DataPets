from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from apps.user.models import Profile

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.review_text
