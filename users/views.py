from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.forms import regForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from smtplib import SMTPException
from django.db.models import F
from django.conf import settings
from django.core.mail import send_mail

User = get_user_model()

def iregister(request):
    if request.method == "POST":
        form= regForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Validate passwords
        if pass1 != pass2:
            messages.error(request, "Passwords do not match. Please try again.")
            return render(request, 'users/register.html')

        # Check for existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists. Please choose a unique email address.")
            return render(request, 'users/register.html')
        #check is account is created
        

        # # Create user with proper username validation (avoid spaces or special characters)
        # username = name.strip()  # Remove leading/trailing whitespaces
        # if not username or username.isalnum():  # Check for alphanumeric characters only
        #     messages.error(request, "Invalid username. Usernames cannot be empty or contain special characters.")
        #     return render(request, 'users/register.html')

        user = User.objects.create(name=name, email=email)
        user.set_password(pass1)
        user.is_active = True
        user.save()
        return redirect('users-login')

        # Authenticate and log in the newly created user (optional)
        # user = authenticate(username=username, password=pass1)
        # if user is not None:
        #     login(request, user)
        #     return redirect('users-login')  # Assuming you have a 'login' URL pattern
    else:
        return render(request, 'users/register.html')

def ilogin(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            get_object_or_404(User, email=email)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request,user)
                messages.success( request, f'Welcome {email}!!')
                return redirect('users-index')
            else:
                 messages.error(request, 'Invalid login credentials')
        except Http404:
            messages.error(request, f'Account with email {email} does not exist. Create account to continue')
        return render(request, 'users/login.html', {'email':email})
    else:      
        return render(request, 'users/login.html')

#@login_required()
def index(request):
    return render(request, 'users/index.html') 
   
def ilogout(request):
    logout(request)
    return redirect('users-login')

def forgot_password(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            user = get_object_or_404(User, email=email)
            user_id = user.id
            user_name = user.name
            activation_link = f'{settings.HOST_ADDRESS}/reset/password/{user_id}'
            subject = 'Reset Password'
            message = f'Hi {user_name}, click the link below to change your password,\n\n{activation_link}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            messages.success(request, 'Request received. Check your email for further instructions')
        except SMTPException:
            messages.error(request, 'Something went wrong. Please try again later.')
        except Http404:
            messages.success(request, 'Request received. Check your email for further instructions')
        except Exception:
            messages.error(request, 'Could not complete your request. Please try again later.')

        return render(request, 'users/forgot_password.html', {'email': email})
    
    return render(request, 'users/forgot_password.html')

def reset_password(request, pk):
    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            try:
                user = get_object_or_404(User, id=pk)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password was reset successfully')
            except Exception:
                messages.error(request, 'Could not complete your request. Please try again later.')
            return redirect('users-login')
        else:
            messages.error(request, 'Passwords did not match.')
            return render(request, 'users/reset_password.html')
    return render(request, 'users/reset_password.html')
       

