from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def food(request):
    obj1 = Product.objects.all()
    return render(request, "index.html", {'products': obj1})


def menu(requst):

    return render(requst,"menu.html")

def gallery(requst):
    return render(requst,"gallery.html")



def productcatdetail(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})