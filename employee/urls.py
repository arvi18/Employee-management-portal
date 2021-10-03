

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name="register"),
    path('profile/', views.profileView, name="profile"),
    path('profile-update/', views.profileUpdateView, name="profile-update"),
    # path('dept/', views.profileView, name="dept"),
    # path('dept/<str:dept_name>/', views.profileView, name="dept_name"),        # redirect to dept
    # path('dept/<str:dept_name>/designation', views.profileView, name="dept_name"),        # public avl  admin spec add/del
    # path('id_card/', views.profileView, name="id_card"),
    # path('payslips/', views.profileView, name="payslips"),      #hardcode salary
    # path('leaves_portal/', views.profileView, name="leaves_portal"),
]
