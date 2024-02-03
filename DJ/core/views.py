from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import items
def products(request):
    context = {
        'items': items.objects.all()
    }
    return render(request, "products.html", context)



def checkout(request):
    context={
        'item':items.objects.all()
    }
    return render(request, 'checkout.html',context)
class homeview(ListView):
    model=items
    template_name='home.html'

class itemview(DetailView):
    model = items
    template_name = "product.html"

