from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import RootForm
from bmain.models import AboutCourse


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = AboutCourse.objects.all()
    if pk:
        root = AboutCourse.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "AboutCourse"
        }
        return render(requests, 'dashboard/aboutc/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "AboutCourse"
    }
    return render(requests, 'dashboard/aboutc/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = RootForm()
    kw = {}
    if pk:
        root = AboutCourse.objects.get(pk=pk)
        form = RootForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = RootForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("aboutc")
    ctx = {
        "form": form,
        "model": "AboutCourse"
    }
    return render(requests, 'dashboard/aboutc/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    AboutCourse.objects.get(pk=pk).delete()
    return redirect("aboutc")
