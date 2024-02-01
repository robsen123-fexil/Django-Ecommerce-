from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import items


def checkout(request):
    context={
        'item':items.objects.all()
    }
    return render(request, 'checkout.html',context)
class homeview(ListView):
    model=items
    template_name='home.html'
def product(request):
    context={
        'item':items.objects.all()
    }
    return render(request,'product.html', context)
      