# Generated by Django 3.1.1 on 2021-03-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0154_auto_20210325_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='discount_dl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='sale',
            name='discount_dl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
        ),
    ]
