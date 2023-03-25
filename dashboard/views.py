from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from bmain.models import Category, Partner, Sifat, Why, AboutCourse, Rating, Teacher, OnlineWork, AboutVacancy
from dashboard.models import User


def sign_in(requests):
    if not requests.user.is_anonymous:
        return redirect('home')

    if requests.POST:
        username = requests.POST.get('username')
        password = requests.POST.get('pass')

        user = User.objects.filter(username=username).first()
        if not user:
            ctx = {
                "error": True
            }
            return render(requests, 'dashboard/regis/login.html', ctx)

        if not user.check_password(password):
            ctx = {
                "error": True
            }
            return render(requests, 'dashboard/regis/login.html', ctx)

        if not user.is_superuser or not user.is_staff:
            ctx = {
                "staff_error": True
            }
            return render(requests, 'dashboard/regis/login.html', ctx)

        login(requests, user)

        return redirect('home')

    ctx = {

    }
    return render(requests, 'dashboard/regis/login.html', ctx)


def sign_out(requests, conf=False):
    if requests.user.is_anonymous:
        return redirect("sign-in")

    if not conf:
        return render(requests, "dashboard/regis/conf_out.html")

    logout(requests)

    return redirect("sign-in")


def index(requests):
    if requests.user.is_anonymous:
        return redirect("sign-in")
    model = [
        ("Category", Category.objects.all().count, "ctg"),
        ("Partner", Partner.objects.all().count, 'part'),
        ("Sifat", Sifat.objects.all().count, 'sifat'),
        ("Why", Why.objects.all().count, 'why'),
        ("About Course", AboutCourse.objects.all().count, 'aboutc'),
        ("Rating", Rating.objects.all().count, 'rate'),
        ("Teacher", Teacher.objects.all().count, 'teach'),
        ("Online Work", OnlineWork.objects.all().count, 'onlinew'),
        ("About Vacancy", AboutVacancy.objects.all().count, 'aboutv'),
    ]

    ctx = {
        "home": True,
        "models": model
    }

    return render(requests, 'dashboard/base.html', ctx)