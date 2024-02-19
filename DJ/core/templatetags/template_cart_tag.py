from core.models import order
from django import template

register=template.Library()
@register.filter
def cart_count(user):
    if user.is_authenticated:
        qs=order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0