from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, Employee_user_profile ,Employee_dept_details, Employee_bank_details, Employee_leaves, Employee_salary
from django import forms


# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver


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