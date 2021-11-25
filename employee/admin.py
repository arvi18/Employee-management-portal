from django.contrib import admin
from .models import *

admin.site.site_header = 'Crager IT solutions pvt limited Admin panel'
admin.site.site_title = 'Crager IT solutions pvt limited'
admin.site.register(Employee)
admin.site.register(Employee_user_profile)
admin.site.register(Employee_dept_details)
admin.site.register(Employee_bank_details)
admin.site.register(Employee_salary)
admin.site.register(Employee_leaves)