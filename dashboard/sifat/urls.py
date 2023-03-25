from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="sifat"),
    path("<int:pk>", list_one, name="sifat_one"),
    path("add/", update_add, name="sifat_add"),
    path("add/<int:pk>", update_add, name="sifat_edit"),
    path("del/<int:pk>", delete, name="sifat_del"),
]
