from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Employee_user(User):
    phone_no=models.CharField(max_length=13)

class Employee_user_profile(Employee_user):
    full_name=models.CharField()
    gender=models.CharField()
    dob=models.DateTimeField
    profile_img=models.ImageField()
    aadhar=models.CharField(max_length=12)
    pan=models.CharField(max_length=10)
    blood_grp=models.CharField(max_length=3)

