from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user == request.user:
        if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profille = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('profile')
   
    return render(request,'update_profile.html',{"form":form})
    
@login_required(login_url='/accounts/login/')
def profile(request)
    current_user = request.user:
    profile = Profile.objects.filter(id = user.id)

    return render(request,'profile.html', {'profile':profile})