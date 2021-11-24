from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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
    blood_group=models.CharField(max_length=3, null=True)
    temporary_address=models.TextField(max_length=200, null=True)
    permanent_address=models.TextField(max_length=200, null=True)
    USERNAME_FIELD='aadhar'

    def __str__(self):
        __full_name=self.profile_personal.user.first_name+ " " +self.profile_personal.user.last_name+ "' s profile"
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
        _name=self.dept_details.user.first_name+ "' s _dept_"
        return _name

class Employee_bank_details(models.Model):
    bank_details=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='bank_details'
    )
    bank_account_no=models.CharField(max_length=12, null=True)
    bank_name=models.CharField(max_length=34, null=True)
    pf_number=models.CharField(max_length=12, null=True)

    def __str__(self):
        _name=self.bank_details.user.first_name+ "' s _bank_"
        return _name

class Employee_salary(models.Model):
    salary_details=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='salary_details'
    )
    net_salary=models.CharField(max_length=12, null=True)
    reimbursement_date=models.DateField(null=True)
    transaction_id=models.CharField(max_length=30, null=True)
    receipt_img=models.ImageField(upload_to='receipts', null=True)
    salary_year=models.SmallIntegerField(default=2021)
    # hardcode

    def __str__(self):
        _name=self.salary_details.user.first_name+ "' s _salary_"
        return _name

class Employee_leaves(models.Model):
    leaves_details=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='leaves_details'
    )
    leaves_count=models.SmallIntegerField(default=20, null=True)
    leaves_type=models.CharField(max_length=30, null=True)
    leaves_from=models.DateTimeField()
    leaves_to=models.DateTimeField()
    # hardcode

    def __str__(self):
        _name=self.leaves_details.user.first_name+ "' s _leaves_"
        return _name

