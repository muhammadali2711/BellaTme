from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import TeacherForm
from bmain.models import Teacher


@staff_member_required(login_url="sign-in")
def list_one(requests, pk=None):
    roots = Teacher.objects.all()
    if pk:
        root = Teacher.objects.get(pk=pk)
        ctx = {
            "root": root,
            "model": "Teacher"
        }
        return render(requests, 'dashboard/teach/detail.html', ctx)
    ctx = {
        "roots": roots,
        "model": "Teacher"
    }
    return render(requests, 'dashboard/teach/list.html', ctx)


@staff_member_required(login_url="sign-in")
def update_add(requests, pk=None):
    form = TeacherForm()
    kw = {}
    if pk:
        root = Teacher.objects.get(pk=pk)
        form = TeacherForm(instance=root)
        kw['instance'] = root

    if requests.POST:
        forms = TeacherForm(requests.POST, requests.FILES, **kw)
        if forms.is_valid():
            forms.save()
            return redirect("teach")
    ctx = {
        "form": form,
        "model": "Teacher"
    }
    return render(requests, 'dashboard/teach/forms.html', ctx)


@staff_member_required(login_url="sign-in")
def delete(requests, pk=None):
    Teacher.objects.get(pk=pk).delete()
    return redirect("teach")
