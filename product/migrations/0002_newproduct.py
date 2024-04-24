# Generated by Django 5.0.2 on 2024-04-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newproduct_img', models.TextField()),
                ('newproduct_name', models.CharField(max_length=50)),
                ('newproduct_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
