from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='DATA DA CRIAÇÃO')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)