from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView,DetailView, View 
from .models import items , orderitem , order
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from .models import items, order, orderitem
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import checkoutforms
from .forms import loginform
from django.template.loader import get_template
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.contrib.auth.forms import UserCreationForm
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
    paginate_by=10
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
            order_item = orderitem.objects.filter(item=item, user=request.user, ordered=False)[0]
            orderuser.items.remove(order_item)
            order_item.delete()
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


def logout(request ):
    return render(request , "login.html")

class cart_summary(View):
    template_name='cart_summary.html'
    def get(self, *args, **kwargs):
          try:
              ordercart=order.objects.get(user=self.request.user, ordered=False)
              context={
                   'object': ordercart,
              }
              return render(self.request, 'cart_summary.html', context)
          except ObjectDoesNotExist: 
             messages.error(self.request ,  "YOU DONT HAVE AN ACTIVE ORDERS")
             return redirect('/')     
class checkoutviews(View):
    def get(self, *args, **kwargs): 
        forms=checkoutforms()
        context={
            'forms':forms
        } 
        return render(self.request, 'checkout.html' , context)
    def post(self, *args, **kwargs):
       form = checkoutforms(self.request.POST or None)
       if form.is_valid():
          print(form.cleaned_data)
          messages.info(self.request, "The checkout is in process")
          return redirect('core:checkoutviews')
       messages.warning(self.request, "the checkout is failed")
       return redirect('core:checkoutviews')

def electronics(request):
    context={
        'items':items.objects.all()
    }
    return render(request, 'electornics.html' , context)
def Sportwear(request):
    context={
        'items':items.objects.all()
    }
    return render(request, 'Sportswear.html' , context)
def shirts(request):
    context={
        'items':items.objects.all()

    }
    return render(request, 'shirts.html' , context)
class searchitem(ListView):
    model = items
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return items.objects.filter(title__icontains=query).order_by('-date')
        else:
            return items.objects.none()
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'login.html' )
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    form=AuthenticationForm(request, request.POST) or None
    if request.method=='POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request , user)
                messages.success(request , f"welcome {username}")
                return render(request , 'home.html')
            else:
                form =AuthenticationForm()
    return render(request , 'login.html', {'form':form})         