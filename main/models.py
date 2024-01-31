from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion_tabla = models.TextField(help_text='Ingrese la descripción tipo tabla')
    ficha_tecnica = models.FileField(upload_to='fichas_tecnicas/', null=True, blank=True)
    datos_texto_varios = models.TextField(help_text='Ingrese datos de texto varios en formato de lista separada por comas', null=True, blank=True)

    def __str__(self):
        return self.nombre