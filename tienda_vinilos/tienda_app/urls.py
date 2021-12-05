from django.urls import path
from .views import home,editar
from .views import home,registro
from .views import home,login2
from .views import home,agregar_producto,listar_productos,eliminar_producto,catalogo, procesar_orden, perfil_producto
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

#URLS donde se registran los templates a usar

urlpatterns = [

    path('', home, name="home"),
    path('contacto/',contacto, name= "contacto"),
    path('editar/<id>',editar, name= "editar"),
    path('login2/',login2, name= "login2"),
    path('registro/',registro, name= "registro"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('agregar-genero/', agregar_genero, name="agregar_genero"),
    path('agregar-artista/', agregar_artista, name="agregar_artista"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lista-productos/',listar_productos, name= "lista_productos"),
    path('eliminar-producto/<id>', eliminar_producto, name = "eliminar_producto"),
    path('catalogo/',catalogo, name= "catalogo"),
    path('editar-productos/<id>', editar_producto, name = "editar_producto"),
    path('update_item/',updateItem, name= "update_item"),
    path('carrito/',carrito, name= "carrito"),
    path('compra/',compra, name= "compra"),
    path('producto-perfil/<id>',perfil_producto, name= "perfil_producto"),
    path ('procesar_orden/',procesar_orden, name="procesar_orden"),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)