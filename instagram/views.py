from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    if current_user == request.user:
        profile = Profile.objects.filter(id = request.user.id)
   
    return render(request,'profile.html',{"profile":profile})
    