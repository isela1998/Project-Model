# Generated by Django 3.1.1 on 2021-02-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0101_auto_20210206_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debts',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Tasa(Bs.)'),
        ),
    ]
