#Archivo para la creacion de tablas en la Base de Datos

from django.db import models
from django.contrib.auth.models import User

#Tabla de Usuarios

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    pais=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

#Tabla de Artistas

class Artista(models.Model):
    nombre = models.CharField(max_length=70)
    imagen = models.ImageField(upload_to="artistas", null=True, blank=True)
    def __str__(self):
        return self.nombre

#Tabla de Generos

class Genero(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

#Tabla de productos

class Producto(models.Model):
    nombre = models.CharField(max_length=70)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT)
    descripcion= models.TextField(max_length=700)
    stock = models.IntegerField()
    precio = models.IntegerField()
    
    imagen = models.ImageField(upload_to="productos", null=True)
    
    
    def __str__(self):
        return self.nombre

#Tabla de Ordenes del carrito

class Orden(models.Model):
    user= models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_orden=models.DateTimeField(auto_now_add=True)
    completo= models.BooleanField(default=False, null=True, blank=True)
    transaccion_id=models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping=False
        ordenproductos = self.ordenproducto_set.all()
        for i in ordenproductos:
            shipping= True
        return shipping

    @property
    def get_cart_total(self):
        ordenproductos = self.ordenproducto_set.all()
        total=sum([producto.get_total for producto in ordenproductos])
        return total
    
    @property
    def get_cart_items(self):
        ordenproductos = self.ordenproducto_set.all()
        total=sum([producto.cantidad for producto in ordenproductos])
        return total
        
#Tabla de procesamiento de Ordenes

class OrdenProducto(models.Model):
    producto= models.ForeignKey(Producto,on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad= models.IntegerField(default=0, null=True, blank=True)
    fecha_agregada = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total=self.producto.precio * self.cantidad
        return total

#Tabla de delivery 

class Shipping(models.Model):
    user= models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, blank=True, null=True)
    orden=models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True)
    ciudad= models.CharField(max_length=200, null=True)
    estado= models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    fecha_agregada= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion