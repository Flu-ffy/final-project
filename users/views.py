from django.shortcuts import redirect, render
from .forms import regForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def ilogin(request):
    return render(request, 'users/login.html')

def iregister(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.create_user(name, email,pass1)
        #Check if passwords match
        if pass1 != pass2 :
            messages.error(request, "Passwords do not match")
            return render(request, 'users/register.html')
        
        #check if email exists
        if User.objects.filter(email = email).first():
            messages.error(request, "An account with this email already exists")
            return render(request, 'users/register.html')
        if User.objects.filter(name =name).first():
            messages.error(request, "This username is already taken")
            return redirect('users-register')
        
        #user=User.objects.create_user(name=name, email=email,password=pass1)
        #user creation
        try:
            user=User.objects.create_user(name=name, email=email,password=pass1)
            user.save()
            messages.success(request, "Account created successfully for {{name.name}}")
            #Takes user to login page
            return redirect('users-login')
        except Exception as e:
            messages.error (request, f'An error occured:{e}')
            return render(request, 'users/register.html')

        # if user_exists:
        #     messages.error(request, 'Member with that email already exists')
    return render(request, 'users/register.html')

def index(request):
    return render(request, 'users/index.html')