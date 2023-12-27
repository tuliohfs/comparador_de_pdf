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
    path('processar_sucafina/', views.processar_sucafina, name='processar_sucafina'),
    path('processar_sucden_rs/', views.processar_sucden_rs, name='processar_sucden_rs'),
    path('processar_sucden_pd/', views.processar_sucden_pd, name='processar_sucden_pd'),
    path('processar_veloso/', views.processar_veloso, name='processar_veloso'),
    path('processar_white/', views.processar_white, name='processar_white'),
    path('processar_mercon/', views.processar_mercon, name='processar_mercon'),  # Adicionada rota para o Mercon
    path('white/', views.white),
    path('sucafina/', views.sucafina),
    path('sucden-pd/', views.sucden_pd),
    path('sucden-rs/', views.sucden_rs),
    path('veloso/', views.veloso),
    path('mercon/', views.mercon),
]
