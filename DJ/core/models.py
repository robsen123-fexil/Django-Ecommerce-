from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
CATEGORIES_CHOICE=(('S', 'shirts'), 
                   ('SW', 'sportshirt') , 
                   ('OW','outwear')
                   )
LABEL_CHOICES=(('p','primary'),
                ('s','secondary'),
                  ('d', 'danger')
                  
                  )
                   
class items(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True, null=True)
    categories=models.CharField(choices=CATEGORIES_CHOICE, max_length=2)
    label=models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug=models.SlugField()
    date=models.DateField(default= timezone.now)
    description=models.CharField(max_length=10000)
    forsell=models.CharField(max_length=100)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("core:remove_from_cart",kwargs={
            'slug':self.slug
        })
class orderitem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , blank=True, null=True)
    ordered=models.BooleanField(default=False)
    item=models.ForeignKey(items, on_delete=models.CASCADE)    
    quality =models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quality} of {self.item.title}"
    
class order(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     items = models.ManyToManyField(orderitem)
     start_date=models.DateTimeField(auto_now_add=True)
     ordered_date=models.DateTimeField()
     ordered=models.BooleanField(default=False)
     
     
     def __str__(self):
         return self.user.username

 
         