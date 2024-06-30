from django.db import models
from django.utils.timezone import now

op=[
    ["Felino","Felino"],
    ["Canino","Canino"],
    ["Ave","Ave"],
    ["Reptil","Reptil"],
    ]

class Mascota(models.Model):
    id_mas = models.IntegerField(primary_key=True)
    tipo_mas = models.CharField(max_length=30,choices=op )
    raza = models.CharField(max_length=30)
    nom_mas = models.CharField(max_length=45)
    fecha_nac = models.DateField()
    foto=models.ImageField(upload_to="MascotaImg",verbose_name="Imagen")
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'mascota'   
         
    def __str__(self):
        texto="{0}"
        return texto.format(self.nom_mas) 


class MascotaServicio(models.Model):
    codigo = models.AutoField(primary_key=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    id_mascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='id_mascota')
    fecha_servicio = models.DateField()

    class Meta:
        managed = False
        db_table = 'mascota_servicio'
        
    

class Servicio(models.Model):
    id_serv = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=70)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="ServicioImg",verbose_name="Imagen")

    class Meta:
        managed = False
        db_table = 'servicio'
        
    def __str__(self):
     texto="{0}"
     return texto.format(self.nom)     
        
class Producto(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nom_pro = models.CharField(max_length=45)
    desc_pro = models.CharField(max_length=60)
    precio = models.FloatField()
    foto =models.ImageField(upload_to="ProductoImg",verbose_name="Imagen")
    stock = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto'
        
    
    def __str__(self):
     texto="{0}"
     return texto.format(self.nom_pro) 



class ProductoUsuario(models.Model):
    codpu = models.AutoField(db_column='codPU', primary_key=True)  # Field name made lowercase.
    id_persona = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_persona')
    id_pro = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_pro')
    cant = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto - usuario'


#AGREGAMOS UN DICCIONARIO CON LAS OPCIONES DEL USUARIO
op=[
    [0,"Administrador"],
    [1,"Cliente"],
    ]

class Usuario(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    user = models.CharField(unique=True, max_length=30, blank=True, null=True)
    pas = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, choices=op)
    nom = models.CharField(max_length=45, blank=True, null=True)
    ape = models.CharField(max_length=45, blank=True, null=True)
    dir = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    foto=models.ImageField(upload_to="BlogImg", null=True, blank=True, verbose_name="Imagen")

    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        texto="{0}"
        return texto.format(self.nom) 

#PARA ESTOS MODELOS IMPORTAMOS LA LIBRERIA TIMEZONE

class Categoria(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre")
    FCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    class Meta:
        verbose_name = "categoría"

    def __str__(self):
        texto="{0}"
        return texto.format(self.nom) 


class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido= models.TextField(verbose_name="Contenido")
    fecha = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    imagen = models.ImageField(upload_to="BlogImg", null=True, blank=True, verbose_name="Imagen")
    id_persona = models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorías")
    Fcreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    Fedicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") 
    
    class Meta:
        verbose_name = "Post"

    def __str__(self):
        texto="{0}"
        return texto.format(self.titulo) 
    
    