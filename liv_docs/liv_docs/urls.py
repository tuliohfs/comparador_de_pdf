from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('', views.index),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('white/', views.white),
    path('sucafina/', views.sucafina),
    path('sucden-pd/', views.sucden_pd),
    path('sucden-rs/', views.sucden_rs),
    path('veloso/', views.veloso),
    path('mercon/', views.mercon),
]
