from django.contrib import admin
from product.models import Product,newProduct

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_cat','product_img','product_name','product_price')
admin.site.register(Product,ProductAdmin)


class NewProductAdmin(admin.ModelAdmin):
    list_display=('newproduct_img','newproduct_name','newproduct_price')
admin.site.register(newProduct,NewProductAdmin)
# Register your models here.
