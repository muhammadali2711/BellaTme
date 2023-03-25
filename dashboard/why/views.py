from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import RootForm
from bmain.models import Why


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = Why.objects.all()
    if pk:
        root = Why.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "Why"
        }
        return render(requests, 'dashboard/why/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "Why"
    }
    return render(requests, 'dashboard/why/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = RootForm()
    kw = {}
    if pk:
        root = Why.objects.get(pk=pk)
        form = RootForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = RootForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("why")
    ctx = {
        "form": form,
        "model": "Why"
    }
    return render(requests, 'dashboard/why/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    Why.objects.get(pk=pk).delete()
    return redirect("why")
