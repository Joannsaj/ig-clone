from django.urls import path
from . import views

urlpatterns=[    
    path('profile/', views.profile, name='profile'),
    path('insta/', views.home, name='home'),
]