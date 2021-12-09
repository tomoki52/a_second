from django.urls import path
from . import views

app_name = "a_second"

urlpatterns = [
    path("", views.index, name="index")
]
