from django.db import models
from django.db.models.base import Model
from PIL import Image


class Employee(models.Model):
    full_name=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=13)
    email=models.EmailField()
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name

class Employee_user_profile(models.Model):
    username_profile=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    gender=models.CharField(max_length=6)
    dob=models.DateField()
    profile_img=models.ImageField(default='default.jpg', upload_to='profile_pics')
    aadhar=models.CharField(max_length=12, unique=True)
    pan=models.CharField(max_length=10, unique=True)
    blood_grp=models.CharField(max_length=3)

    def __str__(self):
        return self.pk

    def save(self, *args, **kwargs):
        super(Employee_user_profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_img.path)