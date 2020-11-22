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
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    
    

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(null=True)
    profile_key = models.ForeignKey('Profile' ,on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-pk"]

    @property
    def get_comments(self):
        return self.comments.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.profile_key.name} Image'

# class Comment(db.Model):
#     __tablename__ = 'comments'

#     comment = db.Column(db.String(255))
#     user_id = models.ForeignKey('Profile' ,on_delete=models.CASCADE)
#     image_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))    
