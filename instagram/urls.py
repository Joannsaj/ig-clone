from django.urls import path
from . import views

urlpatterns=[    
    path('profile/<username>/', views.profile, name='profile'),
    path('updateprofile/', views.update_profile, name='updateProfile'),
    path('home/', views.home, name='home'),
]