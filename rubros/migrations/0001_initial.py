# Generated by Django 5.0.4 on 2024-04-10 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arrendamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('alquiler_base', 'Alquiler Base'), ('servicios_publicos', 'Servicios Públicos'), ('mantenimiento', 'Mantenimiento'), ('impuestos', 'Impuestos'), ('seguro', 'Seguro')], max_length=50)),
                ('frecuencia', models.CharField(max_length=50)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notas_adicionales', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RubroAsignado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('estado_pago', models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado'), ('atrasado', 'Atrasado')], max_length=50)),
                ('notas_adicionales', models.TextField(blank=True, null=True)),
                ('arrendamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrendamientos.arrendamiento')),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rubros.rubro')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_pagado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
                ('metodo_pago', models.CharField(max_length=50)),
                ('comprobante', models.FileField(upload_to='comprobantes/')),
                ('rubro_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rubros.rubroasignado')),
            ],
        ),
    ]
