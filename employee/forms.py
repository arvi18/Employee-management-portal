from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Employee_user, Employee_user_profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.formsets import MAX_NUM_FORM_COUNT

dept= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

role= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

    # label='Department you belong to', widget=forms.Select(choices=dept)
    # label='What is your favorite fruit?', widget=forms.Select(choices=role)

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    birthdate = forms.DateInput()
    phone_no=forms.NumberInput()


    # dept = forms.CharField(label='Department you belong to', widget=forms.Select(choices=dept))
    # role = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=role))

    class Meta:
        model = Employee_user
        fields = ["username", "email", "phone_no", "password1", "password2"]
        # , "role", "birthdate"

class Profile_personal_RegisterForm(UserCreationForm):
    full_name=forms.CharField()
    gender=forms.CharField()
    dob=forms.DateInput()
    profile_img=forms.ImageField()
    aadhar=forms.CharField(max_length=12)
    pan=forms.CharField(max_length=10)
    blood_grp=forms.CharField(max_length=3)

    class Meta:
        model = Employee_user_profile
        fields = ["full_name", "CharField", "gender", "dob", "profile_img", "aadhar", "pan", "blood_grp"]


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






