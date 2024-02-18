from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()

        messages.success(request, "Account created successfully!!")
        return redirect('/signup')
    
    return render(request, 'signup.html')

@login_required(login_url='/signup')

def index(request):
    return render(request, 'index.html')

def loginuser(request):

    if request.method == 'POST':
        # check whether the user credentials are valid
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Could not login.")
            return redirect('/signup')
    
    messages.success(request, "Welcome!!")
    return render(request, 'signup.html')

def logoutuser(request):

    logout(request)
    messages.success(request, "You have been logged out successfully. Kindly login again to continue.")
    return redirect('/signup')