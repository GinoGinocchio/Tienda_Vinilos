from django.shortcuts import get_object_or_404, redirect, render
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,Perfilform,Modform,Productoform
from django.contrib.auth import authenticate,login
from .filters import ProductFilter
from .forms import *
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.http import JsonResponse
import json
import datetime

#Funciones a usar en los templates

#Funciones del home de la pagina

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'tienda_app/home.html', data)

#Funciones de la seccion contacto de la pagina

def contacto(request):

    return render (request, 'tienda_app/contacto.html')

#Funciones del login por defecto de Django

def login1(request):

    return render (request, 'registration/login.html')

#Funciones del Catalogo de productos de la pagina

def catalogo(request):
    context = {}
    #productos = Producto.objects.all()
    myFilter = ProductFilter(
        
        request.GET,
        queryset=Producto.objects.all()
        
    )
    context['myFilter'] = myFilter

    productos_filtrados_paginados  = Paginator(myFilter.qs,6)

    page_numb = request.GET.get('page',1)
    
    person_page_obj = productos_filtrados_paginados.get_page(page_numb)
    context['person_page_obj'] = person_page_obj


    return render(request, 'tienda_app/catalogo.html', context=context)

#Funciones del carrito

def carrito(request):
    if request.user.is_authenticated:
        user = request.user.perfilusuario
        orden, created = Orden.objects.get_or_create(user=user,completo=False)
        productos = orden.ordenproducto_set.all()
    else:
        productos =[]
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    context={'productos': productos, 'orden': orden}
    return render(request, "Producto/carrito.html", context)


def compra(request):
    if request.user.is_authenticated:
        user = request.user.perfilusuario
        orden, created = Orden.objects.get_or_create(user=user,completo=False)
        productos = orden.ordenproducto_set.all()
    else:
        productos =[]
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    context={'productos': productos, 'orden': orden}
    return render(request, "Producto/compra.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action=data['action']

    print('Action:', action)
    print ('productId:', productId)

    user = request.user.perfilusuario
    producto = Producto.objects.get(id=productId)
    orden, created = Orden.objects.get_or_create(user=user,completo=False)

    ordenProducto, created = OrdenProducto.objects.get_or_create(orden=orden, producto=producto)

    if action == 'add':
        ordenProducto.cantidad= (ordenProducto.cantidad+1)
    elif action == 'remove':
        ordenProducto.cantidad = (ordenProducto.cantidad-1)

    ordenProducto.save()

    if ordenProducto.cantidad <= 0:
        messages.error(request,"Producto Eliminado")
        ordenProducto.delete()
    
    return JsonResponse ('Producto fue agregado', safe=False)

#Funciones del procesamiento de ordenes

def procesar_orden(request):

    transaccion_id=datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:

        user = request.user.perfilusuario
        orden, created = Orden.objects.get_or_create(user=user, completo=False)
        total = float(data['form']['total'])
        orden.transaccion_id = transaccion_id

        if total == orden.get_cart_total:
            orden.completo = True
        orden.save()

        if orden.shipping == True:
            Shipping.objects.create(
                user=user,
                orden=orden,
                direccion=data['shipping']['address'],
                ciudad=data['shipping']['city'],
                estado=data['shipping']['state'],
                codigo_postal=data['shipping']['zipcode'],
			)

    else:
	    print('Usuario no registrado')
        
    return JsonResponse('Subiendo Pago', safe=False)


#Funcion de Agregar genero

def agregar_genero(request):
    
    data={
        'form': Generoform()
    }

    if request.method == 'POST':
        formulario= Generoform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Genero Agregado")
        else:
            data["form"] = formulario

    return render (request, 'Producto/agregar_genero.html', data)

#Funcion de agregar artista

def agregar_artista(request):
    
    data={
        'form': Artistaform()
    }

    if request.method == 'POST':
        formulario= Artistaform(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Artista Agregado")
        else:
            data["form"] = formulario

    return render (request, 'Producto/agregar_artista.html', data)

#Funcion de agregar producto

def agregar_producto(request):
    
    data={
        'form': Productoform()
    }

    if request.method == 'POST':
        formulario= Productoform(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado")
        else:
            data["form"] = formulario

    return render (request, 'Producto/agregar_producto.html', data)

#Funcion para el buscar/ filtrar productos

def listar_productos(request):
    context = {}
    #productos = Producto.objects.all()
    myFilter = ProductFilter(
        
        request.GET,
        queryset=Producto.objects.all()
        
    )
    context['myFilter'] = myFilter

    productos_filtrados_paginados  = Paginator(myFilter.qs,6)

    page_numb = request.GET.get('page',1)
    
    person_page_obj = productos_filtrados_paginados.get_page(page_numb)
    context['person_page_obj'] = person_page_obj


    return render(request, 'Producto/lista_productos.html', context=context)

#Funcion para eliminar productos

def eliminar_producto(request,id):

    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, "Producto Eliminado")
    return redirect(to = "lista_productos")

#Funcion para editar producto

def editar_producto(request, id):
    producto= Producto.objects.get(id=id)

    data = {

        'form' : Productoform(instance=producto)
    }

    if request.method == 'POST':
        formulario=Productoform(data=request.POST, instance=producto, files = request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente", redirect(to='lista_productos'))
            data['form'] = Productoform(instance = Producto.objects.get(id=id))
            
    return render(request,'Producto/editar_producto.html' , data)

#Funciones para la edicion de un producto

def perfil_producto(request, id):
    producto= Producto.objects.get(id=id)
 
    context = {

        'id' : producto.id,
        'nombre':producto.nombre,
        'genero' : producto.genero,
        'artista': producto.artista,
        'descripcion': producto.descripcion,
        'stock':producto.stock,
        'precio' : producto.precio,
        'imagen_artista': producto.artista.imagen,
        'imagen' : producto.imagen,
    }
            
    return render(request,'tienda_app/perfil_producto.html' , context)

#Funcion para la edicion de perfil de usuario

def editar(request,id):
    user= PerfilUsuario.objects.get(id=id)
    data={
        'form': Modform(instance=user)
    }
    
    if request.method == 'POST':
        formulario=Modform(data=request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            redirect(to='home')
    else:
        formulario=Modform(instance=user)
    data['form']=formulario 
    return render (request, 'tienda_app/editar.html', data)


#Funcion del login usado por nosotros

def login2(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)      
        if user is not None:
            login(request, user)
            messages.success(request, "Ingreso Correcto")
            return redirect(to="catalogo")
        else:
            messages.error(request, "Contraseña o usario incorrecto")
    context={}
    return render (request, 'tienda_app/login2.html', context)

#Funcion del registro de usuario

def registro(request):
    if request.method == 'POST':  
        form = UserRegisterForm(request.POST)
        perfil_form=Perfilform(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            user=form.save()
            perfil=perfil_form.save(commit=False)
            perfil.user=user
            perfil.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)      
            messages.success(request, "Registro Correcto")
            return redirect(to="catalogo")

    else:
        form=UserRegisterForm()
        perfil_form=Perfilform()   

    data={'form':form, 'perfil_form':perfil_form}
    return render (request, 'tienda_app/registro.html', data)

