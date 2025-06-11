from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

@login_required 
def custom_logout(request):
    logout(request) 
    return render(request, 'users/logout.html') 

@login_required()
def findstore(request):
    return render(request, 'users/store.html')

@login_required()
def featuredproducts(request):
    return render(request,'users/fproducts.html')

def paymentmethod(request):
    return render(request,'users/payment.html')
