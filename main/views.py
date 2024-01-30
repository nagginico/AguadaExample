from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
def about(request):
    return render(request, 'about.html', {})
def cotizacion(request):
    return render(request, 'contact.html', {})
def servicios(request):
    return render(request,'shop.html', {})
def shop(request):
    return render(request, 'shop.html', {})