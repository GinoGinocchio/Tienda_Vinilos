from django.http import request
import django_filters
from django_filters import DateFilter, CharFilter, RangeFilter
from django_filters.filters import *
from .models import * 
from django_filters.widgets import*

#Clase para el buscar/filtrar productos

class MyRangeWidget(RangeWidget):
    def __init__(self, from_attrs={'placeholder': 'Minimo'}, to_attrs={'placeholder': 'Maximo'}, attrs=None):
        super(MyRangeWidget, self).__init__(attrs)

        if from_attrs:
            self.widgets[0].attrs.update(from_attrs)
        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)

class ProductFilter(django_filters.FilterSet):  

    nombre = CharFilter(field_name='nombre',lookup_expr='icontains') 
    precio = RangeFilter(widget=MyRangeWidget(attrs={'min': '0', 'type':'number','max': '1000'}))
    class Meta:

        model = Producto
        fields = ['precio','nombre','genero','artista']


        