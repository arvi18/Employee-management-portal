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

    # overriding save method
    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)
        # using pillow library to deal with images
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
    phone_no=models.CharField(max_length=13, unique=True, null=True)
    gender=models.CharField(max_length=6, null=True)
    dob=models.DateField(null=True)
    aadhar=models.CharField(max_length=12, unique=True, null=True)
    pan=models.CharField(max_length=10, unique=True, null=True)
    blood_grp=models.CharField(max_length=3, null=True)
    USERNAME_FIELD='aadhar'

    def __str__(self):
        __full_name=self.profile_personal.user.first_name+ " " +self.profile_personal.user.last_name
        return __full_name

class Employee_dept_details(models.Model):
    dept_details=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='dept_details'
    )
    dept=models.CharField(max_length=50, null=True)
    role=models.CharField(max_length=50, null=True)
    salary=models.PositiveIntegerField(default=0)
    leaves=models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        _name=self.dept_details.user.first_name+ " " +self.dept_details.user.last_name
        return _name

class Employee_bank_details(models.Model):
    bank_details=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='bank_details'
    )
    bank_acc_no=models.CharField(max_length=12, null=True)
    bank_name=models.CharField(max_length=34, null=True)
    pf_no=models.CharField(max_length=12, null=True)
    temp_address=models.TextField(max_length=200, null=True)
    per_address=models.TextField(max_length=200, null=True)

    def __str__(self):
        _name=self.bank_details.user.first_name+ " " +self.bank_details.user.last_name
        return _name