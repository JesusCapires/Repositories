# Generated by Django 5.0.4 on 2024-04-10 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propiedades', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrendamiento',
            fields=[
                ('id_arrendamiento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('fecha_renovacion', models.DateField(blank=True, null=True)),
                ('duracion', models.CharField(max_length=50)),
                ('monto_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estatus', models.CharField(max_length=50)),
                ('notas', models.TextField(blank=True)),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrendamientos_propiedades', to='usuarios.usuario')),
                ('inquilino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrendamientos_alquilados', to='usuarios.usuario')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrendamientos', to='propiedades.propiedad')),
            ],
        ),
    ]
