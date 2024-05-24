from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def iregister(request):
    if request.method == "POST":
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

        # Create user with proper username validation (avoid spaces or special characters)
        username = name.strip()  # Remove leading/trailing whitespaces
        if not username or username.isalnum():  # Check for alphanumeric characters only
            messages.error(request, "Invalid username. Usernames cannot be empty or contain special characters.")
            return render(request, 'users/register.html')

        user = User.objects.create_user(username=username, email=email, password=pass1)
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
    return render(request, 'users/login.html')