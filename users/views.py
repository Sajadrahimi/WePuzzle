from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import User


# Create your views here.

def show_signup(request):
    if request.user.is_authenticated:
        return redirect('/puzzles')
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def show_login(request):
    if request.user.is_authenticated:
        return redirect('/puzzles')
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def do_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # user = User.objects.get(username = username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/puzzles')
        else:
            print("NOT MATCHED")
            form = LoginForm
            return render(request, 'registration/login.html', {'form': form, 'form_errors':'Username and Password does not match'})
    else:
        return redirect('/login_page')


def do_signup(request):

    if request.method == 'POST':
        User.objects.create_user(username=request.POST['username'],
                                 password=request.POST['password'],
                                 email=request.POST['email'])
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)

        return redirect('/puzzles')


def user_logout(request):
    logout(request)
    return redirect('/')