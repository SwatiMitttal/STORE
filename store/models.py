from django.db import models
from django.urls import reverse
from . import views
# Create your models here.
class Category(models.Model):
    cname=models.CharField(unique=True,max_length=50)
    slug=models.SlugField(unique=True,max_length=30)
    
    
    def __str__(self):
        return self.cname
    def get_url(self):
        return  reverse('prod',args=[self.slug])
class Design(models.Model):
    
    dname=models.CharField(max_length=10,default='jr-1',unique=True)
    dtime=models.CharField(max_length=6,default='')
    im=models.ImageField(upload_to='photos/designs')
    
    def __str__(self):
        return self.dname

class Product(models.Model):
    
    pname=models.CharField(unique=True,max_length=50)
    slug=models.SlugField(unique=True,max_length=30)
    desc=models.CharField(blank=True,max_length=100)
    price=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    avail=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    design=models.ForeignKey(Design,on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.pname
    def get_url(self):
        return  reverse('prod-detail',args=[self.category.slug,self.slug]
                        ,viewname=views.pdetail)
    
    
