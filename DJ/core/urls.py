from django.urls import path


from .views import (
    homeview,
    product,
    checkout,

)
app_name='core'


urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('product/', product, name='product'),
    path('checkout/', checkout,  name='checkout'),
]
