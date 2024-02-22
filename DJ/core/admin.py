from django.contrib import admin

from .models import items , orderitem , order

class orderadmin(admin.ModelAdmin):
    list_display=[ 'user', 'ordered']


admin.site.register(items)
admin.site.register(orderitem)
admin.site.register(order, orderadmin)