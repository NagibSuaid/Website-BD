from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic import View

# Create your views here.

class ContatosListView(View):
    def get(self, request, *args, **kwargs):
        pessoas=Pessoa.objects.all()
        context={
            'pessoas':pessoas
        }
        return render(request,'contatos/listaContatos.html')