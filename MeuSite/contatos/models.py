from django.db import models

# Create your models here.

class Pessoa(models.Model):

    nome = models.CharField(max_length=100, help_text='Entre o nome')
    idade = models.IntegerField(help_text='Entre a idade')
    salario = models.DecimalField(decimal_places=2, max_digits=12 ,help_text='Entre o salário')
    email = models.EmailField(help_text='Entre o email')
    telefone = models.CharField(max_length=20,help_text='Entre o telefone com DDD e DDI')
    dtNasc = models.DateField(verbose_name='Data de nascimento', help_text='Nascimento no formato DD/MM/AAAA')

    def __str__(self):
        return self.nome
