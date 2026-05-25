from django.db import models


class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('electronica', 'Electrónica'),
        ('ropa', 'Ropa'),
        ('alimentos', 'Alimentos'),
        ('hogar', 'Hogar'),
        ('deportes', 'Deportes'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='otro')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre
