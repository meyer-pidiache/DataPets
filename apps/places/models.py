from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Place(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    place_name = models.CharField(max_length = 50)
    place_direction = models.CharField(max_length = 50)
    phoneNumberRegex = RegexValidator(regex = r"^\+?57?\d{8,15}$")
    place_phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, null=True, blank=True)
    place_opening_hours = models.CharField(max_length = 50)
    place_visit_date = models.DateField(null=True, blank=True)
    place_logo = models.ImageField(upload_to='media/places/logo',
                                        default='media/places/logo/default.jpg', 
                                        null=True, blank=True, editable=True)
    place_photo = models.ImageField(upload_to='media/places/photo',
                                        default='media/places/photo/default.jpg', 
                                        null=True, blank=True, editable=True)

    place_logo_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="40")
    place_logo_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="40")
    place_photo_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")
    place_photo_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")

    def __unicode__(self):
        return "{0}".format(self.place_logo)

    def save(self):
        if not self.place_logo:
            return   

        super(Place, self).save()
        image = Image.open(self.place_logo)
        (width, height) = image.size     
        size = ( 40, 40)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.place_logo.path)  
                   
    def __unicode__(self):
        return "{0}".format(self.place_photo)

    def save(self):
        if not self.place_photo:
            return            

        super(Place, self).save()
        image = Image.open(self.place_photo)
        (width, height) = image.size     
        size = ( 200, 200)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.place_photo.path)

    def __str__(self):
        return self.place_name