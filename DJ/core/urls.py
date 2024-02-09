from django.urls import path


from .views import (
    homeview,
    products,
    checkout,
    productall

)
app_name='core'


urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('product/<slug:slug>/', products.as_view() , name='product'),
    path('checkout/', checkout,  name='checkout'),
    path('productall/', productall, name='productall')
]
