from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

@login_required
def accountView(request):
    if request.method == 'POST':
        form_account=employeeAccountForm(request.POST, instance=request.user)
        form_pic = employeeProfilePicForm(request.POST, request.FILES, instance=request.user.employee.profile_personal)
        # form_account=
        if form_account.is_valid() and form_pic.is_valid():
            form_account.save()
            form_pic.save()
            messages.success(request, f'Account details have been succesfully updated.')
            return redirect('account')
    else:
        form_account=employeeAccountForm(instance=request.user)
        form_pic = employeeProfilePicForm(instance=request.user.employee.profile_personal)
    context_forms={
        'form_account':form_account,
        'form_pic':form_pic
    }
    return render(request, 'account.html', context_forms)



def employees_infoView(request):
    employees = Employee_user_profile.objects.all()
    return render(request, 'employees_info.html', {'employees': employees})

@login_required
def profileUpdateView(request):
    if request.method == 'POST':
        form_personal=employee_personal_info(request.POST, instance=request.user.employee.profile_personal)
        form_dept=employee_dept_info(request.POST, instance=request.user.employee.dept_details)
        form_bank=employee_bank_info(request.POST, instance=request.user.employee.bank_details)

        if form_personal.is_valid() and form_dept.is_valid() and form_bank.is_valid():
            form_personal.save()
            form_dept.save()
            form_bank.save()
            messages.success(request, f'Profile has been succesfully updated.')
            return redirect('profile-update')
    else:
        form_personal=employee_personal_info( instance=request.user.employee.profile_personal )
        form_dept=employee_dept_info( instance=request.user.employee.dept_details )
        form_bank=employee_bank_info( instance=request.user.employee.bank_details )

    forms_context={
        'form_personal':form_personal,
        'form_dept':form_dept,
        'form_bank':form_bank
        }
    return render(request, 'update_profile.html', forms_context)    