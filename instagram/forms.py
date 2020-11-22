from django import forms
from .models import Profile, Image, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','name', 'caption')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment')