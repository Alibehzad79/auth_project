from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from accounts_app.forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.


def login_view(request):
    template_name = "accounts/login.html"

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            username = get_user_model().objects.get(email=email).username
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS, message="Login Successfuly."
                )
                return redirect("/")
            else:
                form.add_error("password", "password or email is not valid.")
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, template_name, context)


def register_view(request):
    template_name = "accounts/register.html"

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            password = make_password(password=password1)
            new_user = get_user_model().objects.create(
                username=username, email=email, password=password
            )
            if new_user is not None:
                new_user.save()
                messages.add_message(
                    request, messages.SUCCESS, message="You are registered successfuly."
                )
                return redirect('login')
            else:
                form.add_error("password2", "somthing wrang! please try again.")
    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect("login")
