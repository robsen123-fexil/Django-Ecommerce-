from django.shortcuts import render

from .models import items

def itemlist(request):
    context ={
        'item':items.objects.all(),
    }
    return render(request,'home.html',context)

