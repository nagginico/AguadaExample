from django.shortcuts import render, get_object_or_404
from .models import Producto


# Create your views here.
def index(request):
     # Obtén la lista de productos (o como la obtienes actualmente)
    productos = Producto.objects.all()

    # Realiza las verificaciones antes de pasar a la plantilla
    productos_validos = []
    for producto in productos:
        # Asegúrate de que el ID del producto sea válido
        if producto.id is not None:
            # Agrega el producto a la lista solo si el ID es válido
            productos_validos.append(producto)

    # Pasa la lista filtrada a la plantilla
    return render(request, 'index.html', {'productos': productos_validos})
def about(request):
    return render(request, 'about.html', {})
def cotizacion(request):
    return render(request, 'contact.html', {})
def servicios(request):
    return render(request,'shop.html', {})
def shop(request):
    return render(request, 'shop.html', {})

def producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Procesar la descripción_tabla en la vista
    filas = [fila.split(':') for fila in producto.descripcion_tabla.split('\n') if fila]

    return render(request, 'shop-single.html', {'producto': producto, 'filas': filas})