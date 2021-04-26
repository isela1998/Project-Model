# Generated by Django 3.1.1 on 2021-02-04 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0079_cancelledinvoices_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancelledinvoices',
            name='provider',
        ),
        migrations.AddField(
            model_name='cancelledinvoices',
            name='names',
            field=models.CharField(default=2, max_length=255, verbose_name='Proveedor/Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='datejoined',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='cancelledinvoices',
            name='pay_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='changescanceled',
            name='pay_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='creditnotes',
            name='datejoined',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='end_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha límite'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='start_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='datejoined',
            field=models.DateField(default='2021-02-04', max_length=10),
        ),
        migrations.AlterField(
            model_name='dollarpurchase',
            name='pay_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='next_serv',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Próximo Servicio'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='pay_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='movingproducts',
            name='datejoined',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='officeguideorder',
            name='datejoined',
            field=models.DateField(default='2021-02-04', max_length=10),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='pay_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha de Pago'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='product_warehouse',
            name='date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='admission_date',
            field=models.DateField(default='2021-02-04', max_length=10, verbose_name='Ingreso'),
        ),
    ]
