from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image

class Gender(models.Model):
    description = models.CharField(max_length = 12, null=True, blank=True)

    def __str__(self):
        return self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex = r"^\+?57?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, null=True, blank=True)
    gender = models.ManyToManyField(Gender)
    profile_picture = models.ImageField(upload_to='media/profiles/',
                                        default='media/profiles/default.jpg', 
                                        null=True, blank=True, editable=True,
                                        help_text="_Profile_Picture",
                                        verbose_name="_Profile_Picture")
    profile_picture_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")
    profile_picture_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")

    def __unicode__(self):
        return "{0}".format(self.profile_picture)

    def save(self):
        if not self.profile_picture:
            return            

        super(Profile, self).save()
        image = Image.open(self.profile_picture)
        (width, height) = image.size     
        size = ( 200, 200)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.profile_picture.path)

    def __str__(self):
        return f'{self.user}'