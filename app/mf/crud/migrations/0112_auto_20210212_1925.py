# Generated by Django 3.1.1 on 2021-02-12 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0111_auto_20210212_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelledinvoices',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.providers', verbose_name='Proveedor'),
        ),
    ]
