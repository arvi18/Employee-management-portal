from django.contrib import messages
from django.shortcuts import render, redirect
from employee.models import Employee, Employee_user_profile
from .forms import *

def homeView(req):

    return render(req, "home.html")

def registerView(request):
    if request.method == 'POST':
        form = employeeRegisterForm(request.POST)

        if form.is_valid():
            # saved posted data into User model(default django model with auth)
            form.save()
            # Signals.py stuff here
            # automating deafult profile pic model and blank profile associated.
            username = form.cleaned_data.get('username')
            _get_user=User.objects.get(username=username)
            instance=Employee.objects.create(user=_get_user)
            Employee_user_profile.objects.create(profile_personal=instance)
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