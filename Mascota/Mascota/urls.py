from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as core_views
from Bd_mascotas import views as bd
from Bd_mascotas.views import BlogListView, BlogCreate


urlpatterns = [

    
    #PATHS O DIRECCIONAMIENTO A LAS DEMAS PAGINAS (LOGICA DEL NEGOCIO)
    
    path('admin/', admin.site.urls),
    path('', core_views.main),
    path('contact/', core_views.contacto),
    path('services/', bd.servicios),
    path('portfolio/', bd.portafolio),

    #PATH PARA LOGIN
    path('', include('core.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    
    #CERRAR LA SESION
    path('salir/', core_views.salir, name='salir'),
   
   
   
    path('registro_u/', core_views.registroU),
    
    #CRUD PARA LA TABLA POST
    path('Blog/', BlogListView.as_view(), name='listarPosters'),
    path('Crear/',BlogCreate.as_view(), name='CrearPoster'),
    path('Editar/', bd.posters),
    #path('Editar/<int:pk>/',BlogUpdate.as_view(),name='EditarPoster'),
    
]
    

#CODIGO PARA VERIFICAR LAS IMAGENES CARGADAS
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)