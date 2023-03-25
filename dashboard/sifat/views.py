from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import RootForm
from bmain.models import Sifat


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = Sifat.objects.all()
    if pk:
        root = Sifat.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "Sifat"
        }
        return render(requests, 'dashboard/sifat/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "Sifat"
    }
    return render(requests, 'dashboard/sifat/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = RootForm()
    kw = {}
    if pk:
        root = Sifat.objects.get(pk=pk)
        form = RootForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = RootForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("sifat")
    ctx = {
        "form": form,
        "model": "Sifat"
    }
    return render(requests, 'dashboard/sifat/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    Sifat.objects.get(pk=pk).delete()
    return redirect("sifat")
