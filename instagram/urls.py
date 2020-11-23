from django.urls import path
from . import views

urlpatterns=[    
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.get_profile, name='userProfile'),
    path('home/', views.home, name='home'),
    path('search/', views.search_profile, name='search'),
]