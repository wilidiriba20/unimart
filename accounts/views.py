from django.shortcuts import render, redirect
from .models import User


def login(req):
    if req.method == "POST":
        email = req.POST.get('email').strip()
        password = req.POST.get('password').strip()

        try:
            user = User.objects.get(email=email, password=password)

            req.session['user_id'] = user.id
            req.session['name'] = user.name

            return redirect('index')

        except User.DoesNotExist:
            error = "Invalid email or password"
            return render(req, 'accounts/login.html', {'error': error})

    return render(req, 'accounts/login.html')


def register(req):
    if req.method == "POST":
        name = req.POST.get('name').strip()
        email = req.POST.get('email').strip()
        universty = req.POST.get('university').strip()
        password = req.POST.get('password').strip()

        if not name or not email or not universty or not password:
            return redirect('register')

        user = User(name=name, email=email, password=password, university=universty)
        user.save()

        return redirect('login')

    return render(req, 'accounts/register.html')


def logout(req):
    req.session.flush()
    return redirect('login')