from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView,DetailView
from .models import items , orderitem , order

class products(ListView):
    model=items
    template_name='product.html'
def productall(request):
    context={
        'item':items.objects.all()
    }     
    return render(request , 'product.html' , context)   

def checkout(request):
    context={
        'item':items.objects.all()
    }
    return render(request, 'checkout.html',context)
class homeview(ListView):
    model=items
    template_name='home.html'
def add_to_cart(request, slug):
    item =get_object_or_404(items , slug= slug)
    order_item=orderitem.objects.create(item=item)
    