from django.urls import path
from .views import itemlist


app_name='core'
urlpatterns=[
    path('',itemlist,name='itemlist'),
   
]