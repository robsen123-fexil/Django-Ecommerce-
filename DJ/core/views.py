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

class itemview(DetailView):
    model=items
    template_name='product.html' 
    slug_url_kwarg = 'slug' 