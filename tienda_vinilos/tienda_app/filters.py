import django_filters
from django_filters import DateFilter, CharFilter, RangeFilter
from .models import * 

#Clase para el buscar/filtrar productos

class ProductFilter(django_filters.FilterSet):  

    nombre = CharFilter(field_name='nombre',lookup_expr='icontains') 
    precio = RangeFilter()
    class Meta:

        model = Producto
        fields = ['precio','nombre','genero','artista']



        