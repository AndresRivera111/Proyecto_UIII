from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def carrito(request):
    items = Carrito.objects.all()
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'carrito.html', {'items': items, 'total': total})

def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    item, created = Carrito.objects.get_or_create(producto=producto)
    if not created:
        item.cantidad += 1
    item.save()
    return redirect('index')

def eliminar_carrito(request, item_id):
    item = get_object_or_404(Carrito, id=item_id)
    item.delete()
    return redirect('carrito')
