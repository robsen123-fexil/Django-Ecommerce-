from django.urls import path

from .import views
from .views import (
    homeview,
    products,
    checkoutviews,
    productall,
    add_to_cart,
    remove_from_cart,
   
    logout,
  login_view,
    cart_summary,
    Sportwear,
    
    electronics,
    shirts,
    searchitem,
    signup

)
app_name='core'


urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('product/<slug>/', products.as_view() , name='product'),
    path('productall/', productall, name='productall'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('checkoutviews/' , checkoutviews.as_view(), name='checkoutviews'),
    path('logout/' , logout, name='logout'),
    path('cart_summary/' , cart_summary.as_view(), name='cart_summary'),
    path('Sportwear/' , Sportwear , name='Sportwear'),
    path('elecctronics' , electronics, name='electronics'),
    path('shirts', shirts , name='shirts'),
    path('searchitem/' , searchitem.as_view() , name='searchitem' ),
    path('signup/' , signup , name='signup'),
    path('login_view' , login_view , name='login_view')

]
