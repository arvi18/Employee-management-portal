from django.contrib import messages
from django.shortcuts import render, redirect
from employee.models import *
from .forms import *

def homeView(req):

    return render(req, "home.html")

def loginView(req):
    if req.method=="POST":
        print(req.POST)
    return render(req, "login.html")


def registerView(request):
    if request.method == 'POST':
        form = employeeRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been succesfully created for {username}.')
            return redirect('login')
    else:
        form = employeeRegisterForm()
    return render(request, 'register.html', {'form': form})


def profileUpdateView(request):
    if request.method == 'POST':
        userId=request.user.pk
        currentUser=Employee_personal_info.objects.get(pk=userId)
        form = Employee_personal_info(request.POST, request.FILES, instance=currentUser)

        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been succesfully updated for {username}.')
            return redirect('home')
    else:
        form = Employee_personal_info()
    return render(request, 'register.html', {'form': form})

def profileView(request):
    employees = Employee_user_profile.objects.all()
    return render(request, 'profile.html',{'employees': employees})