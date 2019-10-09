from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil 

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-n//4)
    # params = {'no_of_slides':nSlides,'products':products,'range':range(1,nSlides)}
    # allProds = [[products,range(1,nSlides),nSlides],
    #             [products,range(1,nSlides),nSlides]]

    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-n//4)
        allProds.append([prod,range(1,nSlides),nSlides])

    # print(catprods)




    params = {'allProds':allProds}
    # print(params)
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("this is contact")

def tracker(request):
    return HttpResponse("this is tracker")

def search(request):
    return HttpResponse("this is search")

def productview(request):
    return HttpResponse("this is productview")

def checkout(request):
    return HttpResponse("this is checkout")