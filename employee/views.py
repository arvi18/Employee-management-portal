from django.contrib import messages
from django.shortcuts import render, redirect
from employee.models import Employee, Employee_user_profile, Employee_dept_details, Employee_bank_details
from employee.forms import *
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
            Employee_dept_details.objects.create(dept_details=instance)
            Employee_bank_details.objects.create(bank_details=instance)
            messages.success(request, f'Account has been succesfully created for {username}.')
            return redirect('login')
    else:
        form = employeeRegisterForm()
    return render(request, 'register.html', {'form': form})


def profileUpdateView(request):
    if request.method == 'POST':
        userId=request.user.pk
        currentUser=employee_personal_info.objects.get(pk=userId)
        form = employee_personal_info(request.POST, request.FILES, instance=currentUser)

        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been succesfully updated for {username}.')
            return redirect('home')
    else:
        form = employee_personal_info()
    return render(request, 'register.html', {'form': form})

def profileView(request):
    employees = Employee_user_profile.objects.all()
    employees_depts = Employee_dept_details.objects.all()
    return render(request, 'profile.html', {'employees': employees, 'employees_depts':employees_depts})

def formss(request):
    form_pic=employeeProfilePicForm()
    form_personal=employee_personal_info()
    form_dept=employee_dept_info()
    form_bank=employee_bank_info()
    return render(request, 'forms.html', {'form_pic':form_pic, 'form_personal':form_personal, 'form_dept':form_dept, 'form_bank':form_bank})
    