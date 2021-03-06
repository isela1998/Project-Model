# Generated by Django 3.1.1 on 2021-01-13 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0035_auto_20210111_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='datejoined',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='cancelledinvoices',
            name='pay_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='changescanceled',
            name='pay_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='end_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha límite'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='start_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='datejoined',
            field=models.DateField(default='2021-01-13', max_length=10),
        ),
        migrations.AlterField(
            model_name='dollarpurchase',
            name='pay_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='next_serv',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Próximo Servicio'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='pay_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='movingproducts',
            name='datejoined',
            field=models.DateField(default='2021-01-13, 00:00:00', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='movingproducts',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.companysedes', verbose_name='Sede (Destino)'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='pay_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha de Pago'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='product_warehouse',
            name='date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='admission_date',
            field=models.DateField(default='2021-01-13', max_length=10, verbose_name='Ingreso'),
        ),
    ]
