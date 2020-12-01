from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdate
from django.contrib import messages
from .models import Profile
import os

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,username=username,password=password)

            if not user is None:
                login(request,user)

            messages.add_message(request, messages.SUCCESS, "User is created successfully")
            messages.add_message(request, messages.SUCCESS, "User is login")

            return redirect("login")
        else:
            messages.add_message(request, messages.SUCCESS, "User is not created successfully")

    form = UserRegisterForm()
    return render(request, 'registration/user_register.html', {'form': form})


# def user_logout(request):

#     logout(request)
#     form = UserRegisterForm()

#     return render(request, 'registration/login.html', {'form': form})

@login_required(login_url="login")
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'registration/user_profile.html', {"profile":profile})


def profile_update(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileUpdate(instance=profile)

    if request.method == "POST":
        form = ProfileUpdate(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            print(request)
            if request.FILES.get('user_image', None) != None:
                try:
                    os.remove(profile.user_image.url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)
                profile.user_image = request.FILES['user_image']
                profile.save()
            return redirect("user_profile")
                    

        return redirect('user_profile')

    

    return render(request, 'registration/user_profile_update.html', {'form': form})

