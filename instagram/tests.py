from django.test import TestCase

# Create your tests here.
from .models import Profile, Image
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Joan')
        self.user.save()

        self.new_profile = Profile(id=15, name='image', profile_image='empty.jpg', bio='this is a test',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_image(self):
        self.new_profile.delete_profile()
        users = Profile.objects.all()
        self.assertTrue(len(users) < 1)

class TestImage(TestCase):
    def setUp(self):
        self.new_profile = Profile(name='Joan', user=User(username='jones'))
        self.new_profile.save()

        self.new_image = Image(image='empty.png', image_name='test', image_caption='test', profile_key=self.new_profile)

    def test_insatance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.new_image.delete_image()
        posts = Profile.objects.all()
        self.assertTrue(len(posts) < 1)

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
             