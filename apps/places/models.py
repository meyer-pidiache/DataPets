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
    logo = models.ImageField(upload_to='media/places/logo',
                                        default='media/places/logo/default.jpg', 
                                        null=True, blank=True, editable=True)
    photo = models.ImageField(upload_to='media/places/photo',
                                        null=True, blank=True, editable=True)

    logo_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="40")
    logo_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="40")
    photo_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="422")
    photo_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="324")

    def __unicode__(self):
        return "{0}".format(self.logo)

    def save(self):
        if not self.logo:
            return   

        super(Place, self).save()
        image = Image.open(self.logo)
        (width, height) = image.size     
        size = ( 40, 40)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.logo.path)  
                   
    def __unicode__(self):
        return "{0}".format(self.photo)

    def save(self):
        if not self.photo:
            return            

        super(Place, self).save()
        image = Image.open(self.photo)
        (width, height) = image.size     
        size = ( 422, 314)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)

    def __str__(self):
        return self.name