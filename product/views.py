from django.shortcuts import render, redirect

from .models import *


def product_list(request):
    data = {
        'products': Product.objects.all(),
    }
    return render(request, 'page-list-product.html', data)

def product_add_page(request):
    return render(request, 'page-add-product.html')

def product_add(request):
    name = request.POST.get("name")
    code = request.POST.get("code")
    price = request.POST.get("price")
    incoming = request.POST.get("incoming")
    quantity = request.POST.get("quantity")
    is_active = request.POST.get("is_active")
    measure = request.POST.get("measure")
    if is_active=="on":
        is_active=True
    else:
        is_active=False
    Product.objects.create(code=code, name=name, incoming_price=incoming, price=price, quantity=quantity, is_active=is_active, measure=measure)
    return redirect("/product-list/")

def archive(request):
    data = {
        "products": Product.objects.filter(is_active=False)
    }
    return render(request, "page-list-archive-product.html", data)