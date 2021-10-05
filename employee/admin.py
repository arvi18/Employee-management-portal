from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Employee_user_profile)
admin.site.register(Employee_dept_details)
admin.site.register(Employee_bank_details)