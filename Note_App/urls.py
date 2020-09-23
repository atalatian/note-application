from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.Notes.as_view(), name="index"),
    path("main/add/", views.Add_Notes.as_view(), name="add"),
    path("main/update/<int:pk>/", views.Update_Notes.as_view(), name="update"),
    path("main/delete/<int:pk>", views.Delete_Record.as_view(), name="delete"),
    path("ok/", views.ok, name="ok"),
]
