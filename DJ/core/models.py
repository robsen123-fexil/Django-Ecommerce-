from django.db import models
from django.conf import settings
class items(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    def __str__(self):
        return self.title
class orderitem(models.Model):
    item=models.ForeignKey(items, on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.title
class order(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     items = models.ManyToManyField(orderitem)
     start_date=models.DateTimeField(auto_now_add=True)
     ordered_date=models.DateTimeField()
     ordered=models.BooleanField(default=False)
     
     
     def __str__(self):
         return self.user.username

 
         