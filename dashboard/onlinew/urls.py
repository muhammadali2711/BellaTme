from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="onlinew"),
    path("<int:pk>", list_one, name="onlinew_one"),
    path("add/", update_add, name="onlinew_add"),
    path("add/<int:pk>", update_add, name="onlinew_edit"),
    path("del/<int:pk>", delete, name="onlinew_del"),
]
