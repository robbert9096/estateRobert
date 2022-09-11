from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SingUpForm
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "Your account has been created successfully.")
            login(request,user)
            return redirect('home')
    else:
        form = SingUpForm()
        return render(request, "accounts/register.html", {
            'form' : form
        })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            messages.success(request, "Please try again")
            return redirect('login')
    else:
        return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('home')



def dashboard_user(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {'contacts' : user_contacts}
    return render(request, "accounts/dashboard.html", context)