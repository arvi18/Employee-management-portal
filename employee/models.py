from django.contrib.auth.forms import UsernameField
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser


class Employee(models.Model):
    phone_no=models.CharField(max_length=13, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USERNAME_FIELD='phone_no'

    def __str__(self):
        __full_name=self.user.first_name+ " " +self.user.last_name
        return __full_name

class Employee_user_profile(models.Model):
    profile=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='Profile'
    )
    gender=models.CharField(max_length=6)
    dob=models.DateField()
    profile_img=models.ImageField(default='default.jpg', upload_to='profile_pics')
    aadhar=models.CharField(max_length=12, unique=True)
    pan=models.CharField(max_length=10, unique=True)
    blood_grp=models.CharField(max_length=3)
    USERNAME_FIELD='aadhar'

    def __str__(self):
        __full_name=self.profile.user.first_name+ " " +self.profile.user.last_name
        return __full_name

    def save(self, *args, **kwargs):
        super(Employee_user_profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_img.path)



            
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser


# banking acc nno
# dept
# salary