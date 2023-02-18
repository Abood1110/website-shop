from django.shortcuts import render
from .models import Product

# Create your views here.


def product(requset):
    Pr ={'name':Product.name,
            'price':Product.price,
            'img':Product.image}
    return render(requset, 'products/product.html',{'pro1':Pr})

def products(requset):

    return render(requset, 'products/products.html',{'pro':Product.objects.all(),})
