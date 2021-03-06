from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Employee, Employee_user_profile ,Employee_dept_details, Employee_bank_details, Employee_leaves, Employee_salary
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget, AdminTimeWidget
from django import forms

dept_list= [
    ('IT', 'IT'),
    ('Sales', 'Sales'),
    ('Finance', 'Finance'),
    ('Operations', 'Operations'),
    ('General management', 'General management'),
    ('Strategy', 'Strategy'),
    ('other', 'other')
    ]

role_list= [
    ('CEO', 'CEO'),
    ('COO', 'COO'),
    ('CTO', 'CTO'),
    ('CFO', 'CFO'),
    ('CMO', 'CMO'),
    ('Manager', 'Manager'),
    ('President', 'President'),
    ('Marketing manager', 'Marketing manager'),
    ('Product manager', 'Product manager'),
    ('Finance manager', 'Finance manager'),
    ('Business analyst', 'Business analyst'),
    ('other', 'other')
    ]

class employeeRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email", "password1", "password2"]
    
class employeeAccountForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email"]
    

class employeeProfilePicForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["profile_img"]

class employee_personal_info(forms.ModelForm):
    class Meta:
        model = Employee_user_profile
        fields = ["phone_no", "gender", "dob", "aadhar", "pan", "blood_group", "temporary_address", "permanent_address"]

class employee_dept_info(forms.ModelForm):
    dept=forms.ChoiceField(choices=dept_list, initial='other', required=True)
    role=forms.ChoiceField(choices=role_list, initial='other', required=True)
    class Meta:
        model = Employee_dept_details
        fields = ["dept", "role", "salary"]

class employee_bank_info(forms.ModelForm):
    class Meta:
        model = Employee_bank_details
        fields = ["bank_account_no", "bank_name", "pf_number"]

class employee_bank_info(forms.ModelForm):
    class Meta:
        model = Employee_bank_details
        fields = ["bank_account_no", "bank_name", "pf_number"]

class employee_leaves_info(forms.ModelForm):
    leaves_from=forms.DateField(widget=AdminDateWidget())
    leaves_to=forms.DateField(widget=AdminDateWidget())
    class Meta:
        model=Employee_leaves
        fields=['leaves_from', 'leaves_to', 'leaves_reason', 'leaves_count']
        widgets={
            'leaves_from':AdminDateWidget(attrs={'type': 'date'}),
            'leaves_to':AdminDateWidget()
        }