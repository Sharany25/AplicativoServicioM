# Generated by Django 5.0.7 on 2024-08-19 06:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartilla', '0008_remove_notificacion_fecha_envio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='formulario',
        ),
        migrations.AddField(
            model_name='notificacion',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]