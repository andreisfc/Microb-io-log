from django.urls import path
from mainpage import views

urlpatterns = [
    path("", views.home, name="home")
]