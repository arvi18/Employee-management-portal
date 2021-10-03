from django.contrib.auth.forms import UserCreationForm
from .models import Employee_user_profile
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

# class Employee_personal_info(forms.Form):
#     phone_no=forms.CharField(max_length=14)

#     # dept = forms.CharField(label='Department you belong to', widget=forms.Select(choices=dept))
#     # role = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=role))

#     class Meta:
#         model = Employee_user_profile
#         exclude=["none"]
#         # fields = ["phone_no", "password1", "password2"]
#         #  "username","email", "first_name", "last_name",
#         #  "username", "first_name", "last_name",trrggggggggggggggg

class Employee_profile_personal_info(forms.ModelForm):
    class Meta:
        model = Employee_user_profile
        fields = ["gender", "dob","profile_img", "aadhar", "pan", "blood_grp"]


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


