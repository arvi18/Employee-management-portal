from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, Employee_user_profile
from django import forms


# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser


dept= [
    ('IT', 'IT'),
    ('Sales', 'sales'),
    ('Finance', 'finance'),
    ('Operations', 'operations'),
    ('General management', 'general management'),
    ('Strategy', 'strategy'),
    ]

role= [
    ('CEO', 'CEO'),
    ('Manager', 'Manager'),
    ('President', 'President'),
    ('Marketing manager', 'Marketing manager'),
    ('Product manager', 'Product manager'),
    ('Finance manager', 'Finance manager'),
    ('Business analyst', 'Business analyst'),
    ]

    # label='Department you belong to', widget=forms.Select(choices=dept)
    # label='What is your favorite fruit?', widget=forms.Select(choices=role)

class employeeRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email", "password1", "password2"]

class employeeProfilePicForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["profile_img"]

class Employee_personal_info(forms.ModelForm):
    class Meta:
        model = Employee_user_profile
        fields = ["gender", "dob", "aadhar", "pan", "blood_grp"]


# class Profile_bank_RegisterForm(UserCreationForm):
#     bank_acc_no=
#     bank_name=
#     bank_ifsc_code=
#     pf_acc_no=

# class Profile_address_RegisterForm(UserCreationForm):
#     temp_address=
#     per_address=

# class Profile_dept_RegisterForm(UserCreationForm):
#     dept=
#     designation=
#     phone_no=


