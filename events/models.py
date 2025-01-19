from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    TIPO_EVENTO = [
        ('conferencia', 'Conferência'),
        ('workshop', 'Workshop'),
        ('seminario', 'Seminário'),
    ]
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=100)
    tipo_evento = models.CharField(max_length=20, choices=TIPO_EVENTO)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
