from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index(request):
    context = {}
    return render(request,'index.html',context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+user)
                return redirect('login')

        context = {'form':form}
        return render(request,'accounts/register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, username)
                return redirect('load')
            else:
                messages.info(request,"username or password incorrect")

        context = {}
        return render(request,'accounts/login.html',context)


def logoutPage(request):

    return redirect('index')

@login_required(login_url='login')
def load_lib(request):
    context = {}
    return render(request,'library/load.html',context)

