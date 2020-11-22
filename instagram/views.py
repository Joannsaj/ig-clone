from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment
from .forms import ProfileForm, ImageForm, CommentForm, UserForm
from django.contrib.auth.models import User

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
        form = ImageForm()

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
def profile(request, username):
    # images = request.user.profile.all()
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form, })#'images': images, })

@login_required(login_url='login')
def get_profile(request, username):
    user = get_object_or_404(User, username=username)
    images = user.profile.images.all()

    if request.user == user:
        return redirect('profile', username=request.user.username)
    
    return render(request, 'instagram/user_profile.html', {'user':user, 'images':images})