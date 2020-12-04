from django.urls import path
from mainpage import views

# app_name = 'mainpage'

urlpatterns = [
    path("", views.home, name="home"),
    path("newpost/", views.newpost, name="newpost"),
    path('<int:year>/<int:month>/<slug:slug>/', views.detailedpost, name="detailedpost"),
    path('organisms/<slug:slug>/', views.byorganism, name="byorganism"),
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('logout/', views.logoutpage, name='logout'),
    path('organisms/', views.organisms, name='organisms'),
    path('account/', views.account, name='account'),
]