from django.urls import path

from .views import *

urlpatterns = [
    path("", list_one, name="teach"),
    path("<int:pk>", list_one, name="teach_one"),
    path("add/", update_add, name="teach_add"),
    path("add/<int:pk>", update_add, name="teach_edit"),
    path("del/<int:pk>", delete, name="teach_del"),
]
