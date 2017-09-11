from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=30, null=True, blank=False)
    def __str__(self):
        return self.nome

class PessoaFisica (Pessoa):
    cpf = models.CharField(max_length=11)

class PessoaJuridica (Pessoa):
    cnpj = models.CharField(max_length=11)
    razaoSocial = models.CharField(max_length=100)

class Autor (Pessoa):
    curriculo = models.CharField(max_length=128)
    artigos = models.CharField(max_length=128, null=True)
    pai = models.CharField(max_length=128, null=True)

class Evento (models.Model):
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.CharField(max_length=128)
    nome = models.CharField(max_length=128)
    data_inicio = models.DateTimeField()
    palavrasChave = models.CharField(max_length=128)
    logotipo = models.CharField(max_length=128)
    palavrasChave = models.CharField(max_length=128)
    realizador = models.ForeignKey(PessoaFisica, related_name='realizadores', null=True, blank=False)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    endereco = models.CharField(max_length=250)
    cep = models.CharField(max_length=8)

class EventoCientifico(Evento):
    issn = models.CharField(max_length=9)

 
class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=128)
    evento = models.ForeignKey(EventoCientifico, related_name='evento', null=True, blank=False)
   
class Publicacao(models.Model):
    autor = models.ForeignKey(Autor, related_name='Autor', null=True, blank=False)
    artigo = models.ForeignKey(ArtigoCientifico, related_name='ArtigoCientifico', null=True, blank=False)

# Create your models here.
