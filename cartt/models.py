from django.db import models
from store.models import Product
from django.urls import reverse
# Create your models here.
class Cartt(models.Model):
    ccd=models.CharField(max_length=250,blank=True)
    dadd=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ccd
    
    def get_url(self):
        return reverse('cart',args=[self.ccd])
class Cartitem(models.Model):
    product=models.ForeignKey(Product,models.CASCADE)
    cart=models.ForeignKey(Cartt,models.CASCADE)
    quantity=models.IntegerField(default=0)
    is_alive=models.BooleanField(default=True)
    
    def stot(self):
        return self.product.price*self.quantity
    
    def __str__(self):
        return self.product
    