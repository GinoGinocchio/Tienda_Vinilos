from django.contrib import admin
from .models import PerfilUsuario, Producto, Artista, Genero
from .models import *

# Modelos registrados en la base de datos de Django

admin.site.register(PerfilUsuario)
admin.site.register(Producto)
admin.site.register(Artista)
admin.site.register(Genero)
admin.site.register(Orden)
admin.site.register(OrdenProducto)
admin.site.register(Shipping)