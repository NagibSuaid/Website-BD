from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.http.response import HttpResponseRedirect
from contatos.models import Pessoa
from django.views.generic import View
from contatos.forms import ContatoModelForm

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas=Pessoa.objects.all()
        context={
            'pessoas':pessoas
        }
        return render(request,'contatos/listaContatos.html',context)
    
class ContatoCreateView(View):
    def get(self,request,*args,**kwargs):
        context={'form' : ContatoModelForm}
        return render(request,'contatos/criaContato.html',context)

    def post(self,request,*args,**kwargs):

        form = ContatoModelForm(request.POST)
        if(form.is_valid()):
            contato=form.save()
            contato.save()

            return HttpResponseRedirect(reverse_lazy('contatos:lista'))
        else:
            return HttpResponseRedirect(reverse_lazy('contatos:cria'))