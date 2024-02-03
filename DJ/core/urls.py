from django.urls import path


from .views import (
    homeview,
    itemview,
    checkout,

)
app_name='core'


urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('product/', itemview.as_view(), name='product'),
    path('checkout/', checkout,  name='checkout'),
]
