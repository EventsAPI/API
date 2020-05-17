# Generated by Django 3.0.3 on 2020-05-14 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Eventos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoLocal',
        ),
        migrations.RemoveField(
            model_name='localidad',
            name='asientos_totales',
        ),
        migrations.AddField(
            model_name='asientos',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asientos', to='Eventos.Localidad'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventos',
            name='comentario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventosComent', to='Eventos.Comentarios'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventosLocal', to='Eventos.Localidad'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='valoracion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventosVal', to='Eventos.Valoraciones'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='costo',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localidad',
            name='tipo',
            field=models.SmallIntegerField(choices=[(1, 'Asiento General'), (3, 'Asiento Oro'), (5, 'Asiento Platinum')], default=1),
        ),
        migrations.AddField(
            model_name='valoraciones',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
