# Generated by Django 3.1.1 on 2020-12-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0014_auto_20201220_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='type_exchange',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='type_received',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sale',
            name='change',
            field=models.CharField(default=0.0, max_length=180, verbose_name='Vuelto pendiente'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='exchange',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Cambio'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='received',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Entrada'),
        ),
    ]
