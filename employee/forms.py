from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import tree
from .models import Employee, Employee_user_profile ,Employee_dept_details, Employee_bank_details
from django import forms


# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver


dept_list= [
    ('it', 'IT'),
    ('sales', 'Sales'),
    ('finance', 'Finance'),
    ('operations', 'Operations'),
    ('general management', 'General management'),
    ('strategy', 'Strategy'),
    ('other', 'other')
    ]

role_list= [
    ('ceo', 'CEO'),
    ('manager', 'Manager'),
    ('president', 'President'),
    ('marketing manager', 'Marketing manager'),
    ('product manager', 'Product manager'),
    ('finance manager', 'Finance manager'),
    ('business analyst', 'Business analyst'),
    ('other', 'other')
    ]

class employeeRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email", "password1", "password2"]

class employeeProfilePicForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["profile_img"]

class employee_personal_info(forms.ModelForm):
    class Meta:
        model = Employee_user_profile
        fields = ["phone_no", "gender", "dob", "aadhar", "pan", "blood_grp"]

class employee_dept_info(forms.ModelForm):
    dept=forms.ChoiceField(choices=dept_list, initial='other', required=True)
    role=forms.ChoiceField(choices=role_list, initial='other', required=True)
    class Meta:
        model = Employee_dept_details
        fields = ["dept", "role", "salary"]

class employee_bank_info(forms.ModelForm):
    class Meta:
        model = Employee_bank_details
        fields = ["bank_acc_no", "bank_name", "pf_no", "temp_address", "per_address"]