from django.db import models
from usuarios.models import Usuario
from propiedades.models import Propiedad

class Arrendamiento(models.Model):
    id_arrendamiento = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(null=True, blank=True)
    fecha_renovacion = models.DateField(null=True, blank=True)
    duracion = models.CharField(max_length=50)
    monto_base = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(max_length=50)
    notas = models.TextField(blank=True)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='arrendamientos')
    inquilino = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='arrendamientos_alquilados')
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='arrendamientos_propiedades')
