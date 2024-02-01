from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'inicio'),
    path('about/', views.about, name = 'sobre'),
    path('cotizacion/', views.cotizacion, name='cotizaciones'),
    path('productos/quantium', views.productoQ, name = 'productoQ'),
    path('productos/dieselx10', views.productoD, name = 'productoD'),
]
