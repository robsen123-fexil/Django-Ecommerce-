from django.urls import path


from .views import (
    homeview,
    products,
    checkout,
    productall,
    add_to_cart,
    remove_from_cart

)
app_name='core'


urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('product/<slug>/', products.as_view() , name='product'),
    path('checkout/', checkout,  name='checkout'),
    path('productall/', productall, name='productall'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    
]
