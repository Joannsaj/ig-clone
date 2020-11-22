from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment
from .forms import ProfileForm, ImageForm, CommentForm
# from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user.profile
            image.save()
            return redirect('home')
    else:
        form = PostForm(){
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'index.html', {'images': images, 'form': form, 'users': users })

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    form_class = ProfileForm
    form = form_class(request.POST , request.FILES)
    if request.method == 'POST':
        
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save_profile()
            return redirect('profile')

        else:
            form = ProfileForm()    
   
    return render(request,'update_profile.html',{"form":form})
    
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)

    return render(request,'profile.html', {'profile':profile})