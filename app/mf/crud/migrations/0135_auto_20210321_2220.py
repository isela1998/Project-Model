# Generated by Django 3.1.1 on 2021-03-22 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0134_auto_20210321_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='description',
            field=models.CharField(default='Sin observaciones', max_length=250, verbose_name='Nota'),
        ),
    ]
