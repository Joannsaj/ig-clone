from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile_image = CloudinaryField('image' null=True)
    username = models.ForeignKey(User ,on_delete=models.CASCADE)
    bio = models.TextField(null=True)

class Image(modlels.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(null=True)
    profile_key = models.ForeignKey('Profile' on_delete=models.CASCADE)
    likes = models.BooleanField(null:bool= False)
    comments = models.TextField(null=True)