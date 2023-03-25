from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import RootForm
from bmain.models import Partner


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = Partner.objects.all()
    if pk:
        root = Partner.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "Partner"
        }
        return render(requests, 'dashboard/part/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "Partner"
    }
    return render(requests, 'dashboard/part/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = RootForm()
    kw = {}
    if pk:
        root = Partner.objects.get(pk=pk)
        form = RootForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = RootForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("part")
    ctx = {
        "form": form,
        "model": "Partner"
    }
    return render(requests, 'dashboard/part/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    Partner.objects.get(pk=pk).delete()
    return redirect("part")
