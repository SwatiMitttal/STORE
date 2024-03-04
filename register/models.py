from django.db import models

# Create your models here.
class Account(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    uname=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    mobile=models.CharField(max_length=50)
    
    dadd=models.DateTimeField(auto_now_add=True)
    llogin=models.DateTimeField(auto_now_add=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_sadmin=models.BooleanField(default=False)
    
    UNAME_FIELD='email'
    REQUIRED_FIELDS=['fname','lname','email','mobile']
    
    
    def __str__(self):
        return self.fname+self.lname
