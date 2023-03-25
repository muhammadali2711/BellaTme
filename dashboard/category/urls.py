from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="ctg"),
    path("<int:pk>", list_one, name="ctg_one"),
    path("add/", update_add, name="ctg_add"),
    path("add/<int:pk>", update_add, name="ctg_edit"),
    path("del/<int:pk>", delete, name="ctg_del"),
]
