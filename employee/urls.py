

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('account/', views.accountView, name="account"),
    path('register/', views.registerView, name="register"),
    path('employees-info/', views.employees_infoView, name="employees-info"),
    path('employee-ID/', views.IDView, name="employee-ID"),
    path('profile-update/', views.profileUpdateView, name="profile-update"),
    # path('dept/', views.deptView, name="dept"),
    # path('dept/<str:dept_name>/', views.profileView, name="dept_name"),        # redirect to dept
    # path('dept/<str:dept_name>/designation', views.profileView, name="dept_name"),        # public avl  admin spec add/del
    # path('payslips/', views.profileView, name="payslips"),      #hardcode salary
    path('leaves_portal/', views.leaves_request, name="leaves_portal"),


    # salary model, payroll, leaves

    # 
    # Employee_salary
    # net salary
    # reimbursement_date
    # transaction_id
    # receipt
    # 
    # 
    # Employee_leaves
    # rem leaves count
    # leaves info: leaves from, to
]