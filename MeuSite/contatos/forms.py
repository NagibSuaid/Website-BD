from django import forms
from contatos.models import Pessoa


class ContatoModelForm(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields='__all__'