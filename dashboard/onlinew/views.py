from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import RootForm
from bmain.models import OnlineWork


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = OnlineWork.objects.all()
    if pk:
        root = OnlineWork.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "OnlineWork"
        }
        return render(requests, 'dashboard/onlinew/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "OnlineWork"
    }
    return render(requests, 'dashboard/onlinew/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = RootForm()
    kw = {}
    if pk:
        root = OnlineWork.objects.get(pk=pk)
        form = RootForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = RootForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("onlinew")
    ctx = {
        "form": form,
        "model": "OnlineWork"
    }
    return render(requests, 'dashboard/onlinew/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    OnlineWork.objects.get(pk=pk).delete()
    return redirect("onlinew")
