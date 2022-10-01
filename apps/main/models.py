from django.db import models
from django.utils.timezone import now
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Review(models.Model):
    user = models.ForeignKey(User, 
                        default = 1,
                        null = True, 
                        on_delete = models.CASCADE)
    review_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=now)

    def __str__(self):
        return self.review_text
