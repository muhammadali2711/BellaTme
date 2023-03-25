from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="part"),
    path("<int:pk>", list_one, name="part_one"),
    path("add/", update_add, name="part_add"),
    path("add/<int:pk>", update_add, name="part_edit"),
    path("del/<int:pk>", delete, name="part_del"),
]
