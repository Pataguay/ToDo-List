from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    
    PRIORIDADE_CHOICES = [
        ('baixo', 'Baixo'),
        ('medio', 'Médio'),
        ('alto', 'Alto'),
    ]
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='medio')

    feita = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
