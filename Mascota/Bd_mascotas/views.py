from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .forms import BlogForms

from .models import Servicio, Producto, Post
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


# FBV-->FUNCIONES BASADAS EN VISTAS

def servicios(request):
    servicio= Servicio.objects.all()
    return render(request, "BD_mascotas\services.html", {'servicios':servicio}) 

def portafolio(request):
    producto=Producto.objects.all()
    return render(request, "BD_mascotas\portfolio.html", {'producto':producto})

def posters(request):
    post= Post.objects.all()
    return render(request, "BD_mascotas\editar.html", {'post':post})


#CBV EN LA CRUD: LISTVIEW - POST Y CATEGORIA DEL TEMPLATE BLOG

class BlogListView(ListView):
    model=Post
    paginate_by = 1
    
    def get_queryset(self):
        return Post.objects.all()
    
    #envia informacion adicional la cual sirve para poder paginar
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        return context

#CBV EN LA CRUD: CREATEVIEW - POST Y CATEGORIA DEL TEMPLATE BLOG

class BlogCreate(CreateView):
    model=Post #tabla
    form_class=BlogForms #formulario creado en el forms.py
    template_name='BD_mascotas\CreateBlog.html' #pagina html donde esta el formulario
    success_url=reverse_lazy('listarPosters')
    
    
#CBV EN LA CRUD: UPDATEVIEW - POST Y CATEGORIA DEL TEMPLATE BLOG

#    model=Post #tabla
 #   form_class=BlogForms #formulario creado en el forms.py
  #  template_name='BD_mascotas\UpdateBlog.html' #pagina html donde esta el formulario
   # success_url=reverse_lazy('listarPosters') 
