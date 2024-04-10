from django.db import models
from arrendamientos.models import Arrendamiento

class Rubro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    TIPO_CHOICES = [
        ('alquiler_base', 'Alquiler Base'),
        ('servicios_publicos', 'Servicios Públicos'),
        ('mantenimiento', 'Mantenimiento'),
        ('impuestos', 'Impuestos'),
        ('seguro', 'Seguro'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    frecuencia = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    notas_adicionales = models.TextField(blank=True, null=True)

class RubroAsignado(models.Model):
    arrendamiento = models.ForeignKey(Arrendamiento, on_delete=models.CASCADE)
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    fecha_vencimiento = models.DateField()
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('atrasado', 'Atrasado'),
    ]
    estado_pago = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    notas_adicionales = models.TextField(blank=True, null=True)

class Pago(models.Model):
    rubro_asignado = models.ForeignKey(RubroAsignado, on_delete=models.CASCADE)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=50)
    comprobante = models.FileField(upload_to='comprobantes/')
