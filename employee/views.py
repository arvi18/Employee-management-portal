from django.contrib import messages
from django.shortcuts import render, redirect
from employee.models import Employee_user_profile
from .forms import Employee_profile_personal_info

def homeView(req):

    return render(req, "home.html")

def loginView(req):
    if req.method=="POST":
        print(req.POST)
    return render(req, "login.html")

# def registerView(req):
    # return render(req, "register.html")

def profileUpdateView(request):
    if request.method == 'POST':
        userId=request.user.pk
        currentUser=Employee_user_profile.objects.get(pk=userId)
        form = Employee_profile_personal_info(request.POST, request.FILES, instance=currentUser)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been succesfully updated for {username}.')
            return redirect('login')
    else:
        form = Employee_profile_personal_info()
    return render(request, 'register.html', {'form': form})

def profileView(request):
    employees = Employee_user_profile.objects.all()
    return render(request, 'profile.html',{'employees': employees})