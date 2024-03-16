from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User,Review
from .forms import *


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('logout')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                login(request, user)
                return redirect('addReview')
            else:
                return render(request, 'registration/register.html', {'form':form})
        else:
            return render(request, 'registration/register.html', {'form':RegisterForm()})

def userlogin(request):
    if request.user.is_authenticated:
        print("logout")
        return redirect('logout')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                print(user)
                print("1234568")
                if user is not None:
                    login(request, user)
                    return redirect('myReviews')
                else:
                    return render(request, 'registration/userlogin.html', {'form':form,'error_message': 'Invalid username or password.'})

            else:
                print("is not valid")
                return render(request, 'registration/userlogin.html', {'form':form})
        else:
                return render(request, 'registration/userlogin.html', {'form':LoginForm()})

def userlogout(request):
    logout(request)
    return redirect('login')

def addReview(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddReviewForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                c = Review.objects.create(
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'],
                    creator=user
                )
                return redirect('myReviews')
            else:
                return render(request, 'create.html', {'form':form})
        else:
            return render(request, 'create.html', {'form':AddReviewForm()})
    else:
        return redirect('login')
    
def myReviews(request):#todo just fetch for this user
    reviews = Review.objects.all()
    return render(request, 'myReviews.html', {'reviews':reviews})


