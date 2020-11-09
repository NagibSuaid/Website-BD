from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def homeSec(request):
    return render(request, "registro/homeSec.html")

def registro(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sec-home")
        else:
            context = {
            'form' : form
            }
            return render(request, 'registro/registro.html', context)
    else:
        form = UserCreationForm()
        context = {
            'form' : form
        }
        return render(request, 'registro/registro.html', context)

@login_required
def paginaPerfil(request):
    pass