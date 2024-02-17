from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView,DetailView
from .models import items , orderitem , order
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from .models import items, order, orderitem
from django.contrib import messages
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
    item = get_object_or_404(items, slug=slug)
    order_item, created = orderitem.objects.get_or_create(item=item , user=request.user, ordered=False)
    
    
    order_qs=order.objects.filter(user=request.user ,ordered=False)
    if order_qs.exists():
        orderuser = order_qs[0]
        if orderuser.items.filter(item__slug=item.slug).exists():
            order_item.quality += 1
            order_item.save()
            messages.info(request, "THE PRODUCT IS  UPDATED ")
        else:
            messages.info(request, "THE PRODUCT HAVE BEEN ADDED TO YOUR CART ")
            orderuser.items.add(order_item)
            messages.info(request, "THE PRODUCT HAVE BEEN ADDED TO YOUR CART")
            return redirect("core:product", slug=slug)
    else:
        order_date = timezone.now()
        neworder = order.objects.create(user=request.user, ordered_date=order_date)
        neworder.items.add(order_item)
        messages.info(request, "THE PRODUCT HAVE BEEN ADDED TO YOUR CART  ")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(items, slug=slug)
    order_qs = order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        orderuser = order_qs[0]
        if orderuser.items.filter(item__slug=item.slug).exists():
            
            order_item = orderitem.objects.filter(item=item, user=request.user, ordered=False).first()
            order_item.quality -= 1
            order_item.save()
            messages.info(request, "THE PRODUCT IS REMOVED FROM YOUR CART ")
            if order_item:
                orderuser.items.remove(order_item)
                messages.info(request, "THE PRODUCT WAS NOT ON YOUR Cart")
                return redirect("core:product", slug=slug)
        else:
             messages.info(request, "THE PRODUCT was not ON YOUR CART ")
             redirect("core:product", slug=slug)
             messages.info(request, "THE PRODUCT IS REMOVED FROM YOUR CART ")
    else:
         messages.info(request,"THE PRODUCT IS NOT ON YOUR CART ")
         redirect("core:product", slug=slug)

    return redirect("core:product", slug=slug)
def login_view(request):
    if request=="POST":
        
      
    return render(request, 'login.html')
