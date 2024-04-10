from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=100)  # Se recomienda usar un sistema de autenticación seguro, como Django's built-in User model o JWT.
    TIPO_CHOICES = [
        ('propietario', 'Propietario'),
        ('inquilino', 'Inquilino'),
        ('administrador', 'Administrador'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    num_identificacion = models.CharField(max_length=100)
    rfc = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    notas = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
