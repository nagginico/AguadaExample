from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
def about(request):
    return render(request, 'about.html', {})
def cotizacion(request):
    return render(request, 'contact.html', {})
def combustible(request):
    return render(request,'productos/combustible.html', {})
def productoD(request):
    return render(request, 'dieselinfo.html', {})
def productoQ(request):
    return render(request, 'quantiuminfo.html', {})
def lubricantes(request):
    return render(request, 'productos/lubricantes.html', {})