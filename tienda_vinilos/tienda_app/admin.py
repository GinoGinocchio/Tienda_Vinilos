from django.contrib import admin
from .models import PerfilUsuario, Producto, Artista, Genero
from .models import *
# Register your models here.

admin.site.register(PerfilUsuario)
admin.site.register(Producto)
admin.site.register(Artista)
admin.site.register(Genero)
admin.site.register(Orden)
admin.site.register(OrdenProducto)
admin.site.register(Shipping)