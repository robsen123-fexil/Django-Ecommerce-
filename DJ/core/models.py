from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
CATEGORIES_CHOICE=(('T-shirt', 'shirts'), 
                   ('Electronics', 'Electronics') , 
                   ('SportWear','SportWear')
)

                   
class items(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True, null=True)
    categories=models.CharField(choices=CATEGORIES_CHOICE, max_length=20)
    slug=models.SlugField(unique=True)
    date=models.DateField(default= timezone.now)
    description=models.CharField(max_length=10000)
    forsell=models.CharField(max_length=100)
   
    image=models.ImageField(blank=True , null= True )
    
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
    quantity =models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    def get_total_price(self):
        return self.quantity * self.item.price
    def get_total_discount(self):
        return self.quantity * self.item.discount_price
    
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount()
        else:
            return self.get_total_price()
     
class order(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     items = models.ManyToManyField(orderitem)
     start_date=models.DateTimeField(auto_now_add=True)
     ordered_date=models.DateTimeField()
     ordered=models.BooleanField(default=False)
     
     
     def __str__(self):
         return self.user.username
     def get_total(self):
         total=0
         for product in self.items.all():
             total+=product.get_final_price()
         return total    
     
         