from django.shortcuts import render

from .models import items

def home(request):
    context ={
        'item':items.objects.all(),
    }
    return render(request,'home.html',context)
def checkout(request):
    return render(request, 'checkout.html')
