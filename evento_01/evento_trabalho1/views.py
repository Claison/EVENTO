from django.shortcuts import render
from django.http import HttpResponse
from evento_trabalho1.models import Evento


def listaEvento(request):
    retorno='<h1>Eventos</h1>'
    lista=Evento.objects.all()
    for evento in lista:
        retorno+='</br>Nome do Evento:{}</br>'.format(evento.nome)
    return HttpResponse(retorno)

def get_evento_byID(request,id):
    retorno='<h1>Evento</h1>'
    evento=Evento.objects.get(pk=id)
    retorno +='</br>Nome do Evento:{}</br>'.format(evento.nome)  
    return HttpResponse(retorno)
# Create your views here.
