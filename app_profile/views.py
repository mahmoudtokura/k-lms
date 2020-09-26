from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

# Create your views here.
@login_required
def profile(request):
    context = {
        "user": request.user,
    }
    
    return render(request, 'app_profile/profile.html', context=context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'app_profile/login.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            new_user.set_password(raw_password)
            new_user.save()
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'app_profile/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')