from django.db import models
from usuarios.models import Usuario

class Propiedad(models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    nombre_propiedad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    medidas = models.CharField(max_length=100)
    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('edificio', 'Edificio'),
        ('local_comercial', 'Local Comercial'),
    ]
    tipo_propiedad = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    estatus = models.BooleanField(default=True)
    notas = models.TextField(blank=True)
    costo_base = models.DecimalField(max_digits=10, decimal_places=2)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades_arrendadas')
    inquilino = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades_alquiladas', null=True, blank=True)
