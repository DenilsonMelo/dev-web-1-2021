from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    periodo_ingresso = models.CharField('Perído de Ingresso', max_length=6)
    nota = models.CharField('Nota', max_length=5)
    situacao = models.CharField('Situação', max_length=20)

    def __str__(self):
        return f'{self.nome}'