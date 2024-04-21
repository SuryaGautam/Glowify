from django.http import HttpRequest
from django.shortcuts import render

def home_page(request):
    return render(request,'home.html')

def about_page(request):
    return render(request,'about.html')

def product_page(request):
    return render(request,'product.html')




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