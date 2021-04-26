# Generated by Django 3.1.1 on 2021-01-05 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0020_auto_20210104_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(default='2021-01-04', max_length=10, verbose_name='Fecha de Pago')),
                ('discounts', models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Descuentos')),
                ('desc_discounts', models.CharField(max_length=255, verbose_name='Descripción de Descuentos')),
                ('additional', models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Extras')),
                ('desc_additional', models.CharField(max_length=255, verbose_name='Descripción de Extras')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Total Cancelado')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Notas')),
                ('image', models.FileField(blank=True, null=True, upload_to='Cap_Payroll')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.workers', verbose_name='Trabajador')),
            ],
            options={
                'verbose_name': 'Control de Nómina',
                'verbose_name_plural': 'Control de Nóminas',
                'ordering': ['id'],
            },
        ),
    ]
