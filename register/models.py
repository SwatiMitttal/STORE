from django.db import models
from django.contrib.auth.models import BaseUserManager

class Manager(BaseUserManager):
    def create_user(self,fname,lname,email,passw):
        if not email:
            raise ValueError('PLS ENTER MAIL')
                 
        if not passw:
            raise ValueError('PLS ENTER PASSWORD')
        
        user=self.model
        {email:self.normalize_email(email),
              fname:fname,
              lname:lname}
        #user.set_password(passw)
        return user
        def __str__(self):
            return self.fname+self.lname
    
        
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
