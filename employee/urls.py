

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
    path('payslip/', views.payslipView, name="payslip"),
    path('leaves_portal/', views.leaves_request, name="leaves_portal"),
]