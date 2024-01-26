from django.contrib import admin

from .models import items , orderitem , order
admin.site.register(items)
admin.site.register(orderitem)
admin.site.register(order)