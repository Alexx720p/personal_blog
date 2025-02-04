from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

import logging

logger = logging.getLogger(__name__)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                logger.info(f"User {username} logged in successfully.")
                return redirect('dashboard')
            else:
                logger.warning(f"Authentication failed for user {username}.")
        else:
            form.add_error(None, 'Invalid credentials')
            logger.warning("Form is not valid.")
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 return redirect('dashboard')
#         else:
#             form.add_error(None, 'Invalid credentials')
#     else:
#         form = LoginForm()
#     return render(request, 'authentication/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get['username']
            # raw_password = form.cleaned_data.get['password']
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})
            


def user_status(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'authentication/user_status.html')

