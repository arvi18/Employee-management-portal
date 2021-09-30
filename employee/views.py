from django.http import response
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, Profile_personal_RegisterForm

def homeView(req):

    return render(req, "home.html")

def loginView(req):

    return render(req, "login.html")

# def registerView(req):
    # return render(req, "register.html")

def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been succesfully created for {username}. You are now able to log In.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def profileView(request):
    if request.method == 'POST':
        form_personal_profile = Profile_personal_RegisterForm(request.POST)
        # form_profile = UserRegisterForm(request.POST)
        # form_profile = UserRegisterForm(request.POST)
        # form_profile = UserRegisterForm(request.POST)
        if form_personal_profile.is_valid():
            form_personal_profile.save()
            username = form_personal_profile.cleaned_data.get('username')
            messages.success(request, f'Profile has been succesfully updated for {username}.')
            return redirect('profile')
    else:
        form_personal_profile = Profile_personal_RegisterForm()
    return render(request, 'profile.html', {'form_personal_profile': form_personal_profile})
    

    