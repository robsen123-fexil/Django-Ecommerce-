from django.shortcuts import render

from .models import items

def home(request):
    context ={
        'item':items.objects.all(),
    }
    return render(request,'home.html',context)
def product(request):
    context ={
        'item':items.objects.all(),
    } 
    return render(request, 'product.html' ,context)
def checkout(request):
    context={
        'item':items.objects.all()
    }
    return render(request, 'checkout.html',context)
