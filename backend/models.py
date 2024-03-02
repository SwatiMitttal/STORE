from django.db import models

 #Create your models here.
class Customer(models.Model):
    
       nam=models.CharField(max_length=30,null=False,default='')
       add1=models.CharField(max_length=50,default="")
       mail=models.EmailField(max_length=50,null=False,default='example@gmal.com')
       phone=models.TextField(max_length=12,null=False,default='10 digit number')
       addedat=models.DateTimeField(null=False,default='')
       add2=models.CharField(max_length=100,default='')
       city=models.CharField(max_length=50,default='')
       state=models.CharField(max_length=50,default='')