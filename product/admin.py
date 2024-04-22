from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_cat','product_img','product_name','product_price')
admin.site.register(Product,ProductAdmin)
# Register your models here.
