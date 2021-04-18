from django.shortcuts import render, redirect
from accounts.form import LoginForm, ProfileForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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
                    return redirect('index')
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
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                Profile.objects.create(user=user)
                messages.add_message(request, messages.SUCCESS, "user registered successfully")
                return redirect('login')
            else:
                messages.add_message(request, messages.ERROR, "couldnot register user")
                return render(request, 'ticket/register.html', {'form':form})
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'ticket/register.html', context)

@login_required
def user_account(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Account updated successfully")
            return redirect('profile')
    context = {
        'form': ProfileForm()
    }
    return render(request, 'ticket/profile.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')