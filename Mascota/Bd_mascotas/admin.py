from django.contrib import admin

from .models import Usuario, Mascota, MascotaServicio, Servicio, ProductoUsuario, Producto, Post, Categoria

from django.contrib.auth.admin import UserAdmin



class MascotaAdmin(admin.ModelAdmin):
    list_display= ("id_mas","tipo_mas","raza","nom_mas","fecha_nac","foto","id_usuario") 
admin.site.register(Mascota, MascotaAdmin)
  
class MascotaServAdmin(admin.ModelAdmin):
    list_display= ("codigo","id_servicio", "id_mascota","fecha_servicio")
admin.site.register(MascotaServicio,MascotaServAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display= ("id_serv","nom", "descripcion","precio","imagen")
admin.site.register(Servicio,ServicioAdmin)

class ProductoAdmin(admin.ModelAdmin):   
    #DESPLEGA LOS DATOS DE LA TABLA
    list_display= ("id_pro","nom_pro","desc_pro", "precio","foto","stock")        
admin.site.register(Producto,ProductoAdmin)

class UsuarioAdmin(admin.ModelAdmin):   
    #DESPLEGA LOS DATOS DE LA TABLA
    list_display= ("id_persona","user", "pas","tipo","nom","ape","dir","tel","correo","foto")        
admin.site.register(Usuario,UsuarioAdmin)

class ProdUsuAdmin(admin.ModelAdmin):   
    #DESPLEGA LOS DATOS DE LA TABLA
    list_display= ("codpu","id_persona","id_pro", "cant","total")        
admin.site.register(ProductoUsuario,ProdUsuAdmin)

#CLASES PARA EL BLOG
class BlogAdmin(admin.ModelAdmin):   
    #DESPLEGA LOS DATOS DE LA TABLA
    list_display= ("titulo","contenido","fecha","imagen","Fcreacion", "Fedicion")   
    ordering= ('titulo', 'fecha') 
    list_filter = ('id_persona_id__nom','titulo')    
    
admin.site.register(Post,BlogAdmin)

class CategoriaAdmin(admin.ModelAdmin):   
    #DESPLEGA LOS DATOS DE LA TABLA
    list_display= ("nom","FCreacion")        
admin.site.register(Categoria,CategoriaAdmin)
 
    