from django.shortcuts import render, HttpResponse, redirect
from django.template import loader

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required


def salir(request):
    logout(request)
    return redirect('/')

def main(request):
    template=loader.get_template('core\index.html')
    return HttpResponse(template.render()) 

def contacto(request):
    return render(request, "core\contact.html")


def login(request):
    return render(request, "core\ingresar.html")

def registroU(request):
    return render(request, "core\Registro_u.html")
