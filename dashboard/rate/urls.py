from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="rate"),
    path("<int:pk>", list_one, name="rate_one"),
    path("add/", update_add, name="rate_add"),
    path("add/<int:pk>", update_add, name="rate_edit"),
    path("del/<int:pk>", delete, name="rate_del"),
]
