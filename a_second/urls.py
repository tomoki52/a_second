from os import name
from django.urls import path
from . import views

app_name = "a_second"

urlpatterns = [
    path("clock/", views.clock, name="clock"),
    path("", views.input, name="input")
]
