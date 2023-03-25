from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import RootForm
from bmain.models import AboutVacancy


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = AboutVacancy.objects.all()
    if pk:
        root = AboutVacancy.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "AboutVacancy"
        }
        return render(requests, 'dashboard/aboutv/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "AboutVacancy"
    }
    return render(requests, 'dashboard/aboutv/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = RootForm()
    kw = {}
    if pk:
        root = AboutVacancy.objects.get(pk=pk)
        form = RootForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = RootForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("aboutv")
    ctx = {
        "form": form,
        "model": "AboutVacancy"
    }
    return render(requests, 'dashboard/aboutv/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    AboutVacancy.objects.get(pk=pk).delete()
    return redirect("aboutv")
