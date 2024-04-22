from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Fecha de registro')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Fecha de registro')
    stock = models.PositiveIntegerField(default=0)
    imagen_url = models.URLField(default='https://www.libreriahuequito.com/public/images/productos/default.png')

    def __str__(self):
        return self.nombre

