from django.http import HttpRequest
from django.shortcuts import render
from product.models import Product,newProduct
from contactenquiry.models import ContactEnquiry

def home_page(request):
    product_data=newProduct.objects.all()
    data=[]
    for product in product_data:
        product_data={
            "image":product.newproduct_img,
            "product_name":product.newproduct_name,
            "price":product.newproduct_price
        }
        data.append(product_data)
    return render(request,'home.html',{"newproduct":data})

def about_page(request):
    return render(request,'about.html')

def product_page(request):
    product_data=Product.objects.all()
    data=[]
    for product in product_data:
        product_data={
            "category":product.product_cat,
            "image":product.product_img,
            "product_name":product.product_name,
            "price":product.product_price
        }
        data.append(product_data)
    return render(request,'product.html',{"product":data})

def contact_page(request):
    try:
        if request.method=="POST":
            if request.POST["name"] == "":
                return render(request,'contact.html',{"error":True,"name":"Name"})  
            elif request.POST["email"] == "":
                return render(request,'contact.html',{"error":True,"name":"E-mail"})
            elif request.POST["phonenumber"] == "":
                return render(request,'contact.html',{"error":True,"name":"Phone Number"})
            else:
                return render(request,'contact.html')    
    except:
        pass

    return render(request,'contact.html')

def save_enquiry(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phonenumber=request.POST["phonenumber"]
        message=request.POST["message"]
        data=ContactEnquiry(name=name,email=email,phone_number=phonenumber,message=message)
        data.save()
    return render(request,"thankyou.html")
    

