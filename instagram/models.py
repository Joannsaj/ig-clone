from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile_image = CloudinaryField('image' null=True)
    username = models.CharField(max_length=30)
    bio = models.TextField(null=True)