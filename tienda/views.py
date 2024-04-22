from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Producto 
from .models import Categoria

def index(request):
    product_list = Producto.objects.all()
    categoria_list = Categoria.objects.all()  # Obteniendo todas las categorías
    context = {
        'product_list': product_list,
        'categoria_list': categoria_list,  # Pasando la lista de categorías al contexto
    }
    return render(request, 'index.html', context)


def producto(request):
    return render(request, 'producto.html')


def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()  # Obtener todas las categorías para mostrar la lista
    context = {
        'categoria': categoria,
        'productos': productos,
        'categoria_list': categorias,  # Pasar la lista de categorías al contexto
    }
    return render(request, 'productos_por_categoria.html', context)