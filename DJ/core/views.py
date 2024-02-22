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

def login_view(request):
    if request=='POST':
        username=request.POST['username']
        password=request.POST['password']
        remember_me=request.POST.get('remember_me', False)
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        

        else:
            messages.error(request, "Invalid Password Or Username")
    return render(request, 'login.html')
def logout(request ):
    return render(request , "login.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
       
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "password is not same")
                return redirect ('homeview')
            if User.objects.filter(email=email).exists():
                messages.error(request, "email is already taken ")
                return redirect('homeview')
            else:
                user=User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('homeview')
        else:
            messages.error(request, "password is not same ")

    else:    
       return render(request, 'signup.html')

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

    