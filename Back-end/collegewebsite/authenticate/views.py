from .forms import UpdateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

# utility functions
def check_username(username):
    try:
        user = User.objects.get(username = username)
        return True
    
    except User.DoesNotExist:
        return False

def check_email(email):
    try:
        user = User.objects.get(email = email)
        return True
    
    except User.DoesNotExist:
        return False
    
# Create your views here.

def signin(request):

    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')

        if firstname != '' and lastname != '' and email != '':
            
            if password == confirmpassword:

                    username_flag = check_username(username)
                    email_flag = check_email(email)
                    
                    if username_flag == True:
                        messages.error(request, 'Username already in use.')
                        return redirect('/signin')
                    
                    elif email_flag == True:
                        messages.error(request, 'Email already registered.')
                    
                    elif username_flag == False and email_flag == False:
                        user = User.objects.create_user(first_name = firstname, last_name= lastname, username = username, email = email, password = password)
                        user.save()

                        messages.success(request, "Account created successfully!!")
                        return redirect('/signin')             
        
            else:
                messages.error(request, 'Both password and Confirm password fields have to be same.')
                return redirect('/signin')
        
        else:
            messages.error(request, "Please fill the complete form.")
            return redirect('/signin')
    
    return render(request, 'signin.html')

@login_required(login_url='/signin')

def index(request):
    return render(request, 'index.html')

def loginuser(request):

    if request.method == 'POST':
        # check whether the user credentials are valid
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            messages.error(request, "Please fill the form.")
            return redirect('/signin')
        else:
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
            
            elif user is None:
                messages.error(request, "No user with such Credentials.")
                return redirect('/signin')
            
            else:
                messages.error(request, "Could not login.")
                return redirect('/signin')

    return render(request, 'signin.html')

def logoutuser(request):

    logout(request)
    messages.success(request, "You have been logged out successfully. Kindly login again to continue.")
    return redirect('/signin')

def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        
        if user_form.is_valid():
            user_form.save()
            
            user = User.objects.get(username = request.user)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            if first_name != user.first_name:
                user.first_name = first_name
                user.save()

            elif last_name != user.last_name:
                user.last_name = last_name
                user.save()

            messages.success(request, 'Account Details Updated successfully.')
            return redirect('/profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
                
    return render(request, 'profile.html', {'user_form':user_form})

def change(request):
    if request.method == 'POST':
        
        old_password = request.user.password
        print(old_password)

        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            try:
                user = User.objects.get(username = request.user)
                user.set_password(f'{new_password}')
                user.save()

                messages.success(request, 'Your password changed successfully!!')
                return redirect('/signin')
            
            except Exception as error:
                messages.error(request, f'Error: {error}')
                return redirect('change_password')
    
    return render(request, 'change_password.html')