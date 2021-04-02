from django.shortcuts import render, redirect
<<<<<<< HEAD
from accounts.form import LoginForm, RegisterForm
=======
<<<<<<< HEAD
from accounts.form import LoginForm, ProfileForm
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from accounts.auth import unauthenticated_user
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

@unauthenticated_user
def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(request, username=data['username'], password=data['password'])
                if user is not None:
                    login(request, user)
                    redirect('index')
                else:
                    messages.add_message(request, messages.ERROR, "Provided credintials are not correct")
                    return render(request, 'ticket/login.html', {'form':form})
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'ticket/login.html', context)
        
@unauthenticated_user
def user_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "user registered successfully")
                return redirect('login')
            else:
                messages.add_message(request, messages.ERROR, "couldnot register user")
                return render(request, 'ticket/register.html', {'form':form})
        form = UserCreationForm
        context = {
            'form': form
        }
        return render(request, 'ticket/register.html', context)
# def user_account(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Account updated successfully")
#             return redirect('/')
#     context = {
#         'form': form
#     }
#     return 
=======
from accounts.form import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "logged on")
                return redirect('')
            else:
                messages.add_message(request, messages.ERROR, "username or password is incorrect")
                return render(request, 'ticket/login.html', {'form': form})
    form = LoginForm
    context={
        'form':form
    }
    return render(request, 'ticket/login.html', context)

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "user registered successfully")
            return redirect('')
        else:
            messages.add_message(request, messages.ERROR, "couldnot register user")
            return render(request, 'ticket/register.html', {'form':form})
    form = UserCreationForm
    context = {
        'form': form
    }
    return render(request, 'ticket/register.html', context)
>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9

def user_logout(request):
    logout(request)
<<<<<<< HEAD
    return redirect('login')
=======
    return redirect('login')

>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9
