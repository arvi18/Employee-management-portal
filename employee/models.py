from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser


class Employee(models.Model):
    profile_img=models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        _user_name=self.user.username+ " (" + self.user.first_name + ")"
        return _user_name

    
    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)

        img = Image.open(self.profile_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_img.path)


class Employee_user_profile(models.Model):
    profile_personal=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='profile_personal'
    )
    phone_no=models.CharField(max_length=13, unique=True, blank=True)
    gender=models.CharField(max_length=6)
    dob=models.DateField()
    aadhar=models.CharField(max_length=12, unique=True)
    pan=models.CharField(max_length=10, unique=True)
    blood_grp=models.CharField(max_length=3)
    USERNAME_FIELD='aadhar'

    def __str__(self):
        __full_name=self.profile_personal.user.first_name+ " " +self.profile_personal.user.last_name
        return __full_name
