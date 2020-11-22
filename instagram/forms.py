from django import forms
from .models import Profile, Image, Comment
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','image_name', 'image_caption',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class UserForm(forms.ModelForm):
    class Meta:

        model = User
        fields = ('email',)        