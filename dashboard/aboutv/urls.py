from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="aboutv"),
    path("<int:pk>", list_one, name="aboutv_one"),
    path("add/", update_add, name="aboutv_add"),
    path("add/<int:pk>", update_add, name="aboutv_edit"),
    path("del/<int:pk>", delete, name="aboutv_del"),
]
