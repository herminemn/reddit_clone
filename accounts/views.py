# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'This username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/login.html', {'error': 'SignUp Successful'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords don\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def log_in(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'accounts/login.html', {'error': 'LogIn Successful'})
        else:
            return render(request, 'accounts/login.html', {'error': 'The Username or Password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')
