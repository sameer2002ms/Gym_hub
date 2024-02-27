from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.decorators import login_required



# Create your views here.


def login_page(request):
    context = {'page_name': 'Login Page'}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if not user.exists():
            messages.error(request, 'First Register Email Id')
            # return redirect('account/login.html')
            return HttpResponseRedirect(request.path_info)

        # if not user[0].profile.is_email_verified:
        #     messages.warning(request, 'Your account is not verified')
        #     return HttpResponseRedirect(request.path_info)

        user = authenticate(username=username, password=password)

        if user is None:
            messages.warning(request, 'Invalid password')
            # return redirect('account/login.html')
            return HttpResponseRedirect(request.path_info)

        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', context)


def register_page(request):
    context = {'page_name': 'Register Page'}

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


# here we are checking the unique user
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Email already taken')
            # return redirect('account/register.html')
            return HttpResponseRedirect(request.path_info)

# here we are creating the object
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
# here we are saving the password in the form of encryption
        user.set_password(password)
        user.save()

        # messages.success(request, 'An Email has been sent on your mail.')
        # return HttpResponseRedirect(request.path_info)

        # return redirect('account/register.html')

    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/account/login')
def User_dashbaord(request):
    return render(request, 'dashboard.html', {'page_name' : 'Dashboard Page'})



def edit_profile(request):
    msg = None
    if request.method == "POST":
        form = forms.ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            msg = 'Data has been Updated. Thank You'
    form = forms.ProfileForm(instance=request.user)        
        
    return render(request, 'edit_profile.html', {'form':form, 'msg' : msg, 'page_name' : 'Editprofile Page'})

    
