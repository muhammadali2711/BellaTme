from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import RootForm
from bmain.models import Rating


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = Rating.objects.all()
    if pk:
        root = Rating.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "Rating",
            "rating": root.rating * "⭐"
        }
        return render(requests, 'dashboard/rate/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "Rating"
    }
    return render(requests, 'dashboard/rate/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = RootForm()
    kw = {}
    if pk:
        root = Rating.objects.get(pk=pk)
        form = RootForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = RootForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("rate")
    ctx = {
        "form": form,
        "model": "Rating"
    }
    return render(requests, 'dashboard/rate/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    Rating.objects.get(pk=pk).delete()
    return redirect("rate")
