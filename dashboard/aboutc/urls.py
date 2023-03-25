from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="aboutc"),
    path("<int:pk>", list_one, name="aboutc_one"),
    path("add/", update_add, name="aboutc_add"),
    path("add/<int:pk>", update_add, name="aboutc_edit"),
    path("del/<int:pk>", delete, name="aboutc_del"),
]
