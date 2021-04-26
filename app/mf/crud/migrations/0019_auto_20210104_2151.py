# Generated by Django 3.1.1 on 2021-01-05 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0018_auto_20210101_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangesCanceled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha')),
                ('names', models.CharField(max_length=255, verbose_name='Nombre y Apellido')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Cantidad ($$)')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('image', models.FileField(blank=True, null=True, upload_to='Cap_Dollars')),
            ],
            options={
                'verbose_name': 'Vuelto Cancelado',
                'verbose_name_plural': 'Vueltos Cancelados',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='cancelledinvoices',
            name='pay_date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='end_date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha límite'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='start_date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='dollarpurchase',
            name='pay_date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='next_serv',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Próximo Servicio'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='pay_date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='product_warehouse',
            name='date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='admission_date',
            field=models.DateField(default='2021-01-04', max_length=10, verbose_name='Ingreso'),
        ),
    ]
