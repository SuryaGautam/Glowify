from django.db import models
class Product(models.Model):
    product_cat=models.CharField(max_length=50)
    product_img=models.TextField()
    product_name=models.CharField(max_length=50)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
# Create your models here.
