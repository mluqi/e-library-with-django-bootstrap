from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return render(request, "users/register.html", {"message": "User already logged in", "hide_form": True})
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("catalog:list")
    else:
        form = UserCreationForm()
        
    return render(request, "users/register.html", { "form":form, "hide_form": False })

def login_view(request):
    if request.user.is_authenticated:
        return render(request, "users/login.html", {"message": "User already logged in",   "hide_form": True})
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("catalog:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form":form })

@login_required(login_url="/users/login/")
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("catalog:list")

