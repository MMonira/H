from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import CustomUser
from app.forms import CustomrUserForm, customAuthForm

def signupformpage(request):
    if request.method == 'POST':
        form = CustomrUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup Successful')
            return redirect('signinformpage')
    else:
        form = CustomrUserForm()
    return render(request, 'signupformpage.html', {'form': form})

def signinformpage(request):
    if request.method == 'POST':
        signinform = customAuthForm(request, data=request.POST)
        if signinform.is_valid():
            user = signinform.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        signinform = customAuthForm()
    return render(request, 'signinformpage.html', {'form': signinform})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
