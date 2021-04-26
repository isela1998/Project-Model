# Generated by Django 3.1.6 on 2021-04-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0159_auto_20210329_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banktransfers',
            name='pay_date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='datejoined',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='cancelledinvoices',
            name='pay_date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='end_date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha límite'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='start_date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='dollarhistory',
            name='datejoined',
            field=models.CharField(default='2021-04-26', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='historyoperations',
            name='datejoined',
            field=models.CharField(default='2021-04-26', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='datejoined',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='pay_date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='services',
            name='datejoined',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='date',
            field=models.DateField(default='2021-04-26', max_length=10, verbose_name='Fecha'),
        ),
    ]
