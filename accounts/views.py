from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.db import IntegrityError

User = get_user_model()

def register(request):
    if request.method == "POST":
        full_name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").lower().strip()
        university = request.POST.get("university", "").strip()
        password = request.POST.get("password", "")
        confirm = request.POST.get("confirm", "")

        if password != confirm:
            return render(request, "accounts/register.html", {"error": "Passwords do not match"})

        # Split full name
        parts = full_name.split(maxsplit=1)
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ""

        if User.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {"error": "Email already registered"})

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            university=university
        )

        # ✅ Correct login
        auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return redirect("index")

    return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email", "").lower().strip()
        password = request.POST.get("password", "")

        user = authenticate(request, email=email, password=password)
        if user:
            auth_login(request, user)
            return redirect("index")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid email or password"})

    return render(request, "accounts/login.html")


def logout(request):
    auth_logout(request)
    return redirect('login')