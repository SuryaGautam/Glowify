# Generated by Django 5.0.2 on 2024-04-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_newproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newproduct',
            name='newproduct_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]