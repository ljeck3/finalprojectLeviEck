from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back, %s!' % user.username)
            return redirect('home')  # this should be the name of your home page URL
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'authenticate/login.html')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)  # This logs the user out
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful! Welcome, %s!' % user.username)
            return redirect('home')  # Redirect to home page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })