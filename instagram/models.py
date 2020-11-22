from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_image = CloudinaryField('image', null=True)
    name = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()
    

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(null=True)
    profile_key = models.ForeignKey('Profile' ,on_delete=models.CASCADE)
    likes = models.BooleanField(null= True)
    comments = models.TextField(null=True)

# class Comment(db.Model):
#     __tablename__ = 'comments'

#     comment = db.Column(db.String(255))
#     user_id = models.ForeignKey('Profile' ,on_delete=models.CASCADE)
#     image_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))    
