
from django.urls import path
from .views import main, login



urlpatterns = [
        
    #PATH PARA LOGIN   
   
    path('', main),
    path('ingresar/', login),
    #path('productos/', products),
    
    
]