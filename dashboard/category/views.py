from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import CtgForm
from bmain.models import Category


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = Category.objects.all()
    if pk:
        root = Category.objects.get(pk=pk)
        ctx = {
            "root": root
        }
        return render(requests, 'dashboard/ctg/detail.html', ctx)
    ctx = {
        "roots": roots
    }
    return render(requests, 'dashboard/ctg/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = CtgForm()
    kw = {}
    if pk:
        root = Category.objects.get(pk=pk)
        form = CtgForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = CtgForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("ctg")
    ctx = {
        "form": form
    }
    return render(requests, 'dashboard/ctg/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    Category.objects.get(pk=pk).delete()
    return redirect("ctg")
