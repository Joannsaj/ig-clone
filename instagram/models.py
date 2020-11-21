from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_image = CloudinaryField('image', null=True)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.username

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(null=True)
    profile_key = models.ForeignKey('Profile' ,on_delete=models.CASCADE)
    likes = models.BooleanField(null= True)
    comments = models.TextField(null=True)