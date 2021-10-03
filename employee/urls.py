from django.urls import path
from Employee_management import settings
from . import views;
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homeView, name="home"),
    path('login/', views.loginView, name="login"),
    path('register/', views.profileUpdateView, name="register"),
    path('profile-update/', views.profileUpdateView, name="profile-update"),
    path('profile/', views.profileView, name="profile"),
    path('dept/', views.profileView, name="dept"),
    # path('dept/<str:dept_name>/', views.profileView, name="dept_name"),        # redirect to dept
    # path('dept/<str:dept_name>/designation', views.profileView, name="dept_name"),        # public avl  admin spec add/del
    # path('id_card/', views.profileView, name="id_card"),
    # path('payslips/', views.profileView, name="payslips"),      #hardcode salary
    # path('leaves_portal/', views.profileView, name="leaves_portal"),
]
