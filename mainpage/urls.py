from django.urls import path
from mainpage import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newpost/", views.newpost, name="newpost"),
    path('<int:year>/<int:month>/<slug:slug>/', views.detailedpost, name="detailedpost"),
]