from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="why"),
    path("<int:pk>", list_one, name="why_one"),
    path("add/", update_add, name="why_add"),
    path("add/<int:pk>", update_add, name="why_edit"),
    path("del/<int:pk>", delete, name="why_del"),
]
