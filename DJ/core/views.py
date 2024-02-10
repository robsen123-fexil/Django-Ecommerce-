from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView,DetailView
from .models import items , orderitem , order
from django.shortcuts import redirect
from django.utils import timezone
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
    order_item,created= orderitem.objects.get_or_create(item=item , user=request.user, ordered=False)
    order_qs = order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        orderuser = order_qs[0]
        if orderuser.items.filter(item__slug=item.slug).exists():
            order_item.quality += 1
            order_item.save()
        else:
            orderuser.items.add(order_item)
    else:
        order_date = timezone.now()
        neworder = order.objects.create(user=request.user, ordered_date=order_date)
        neworder.items.add(order_item)

    return redirect("core:product", slug=slug)