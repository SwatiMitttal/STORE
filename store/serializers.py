from rest_framework import serializers
from .models import Product,Category


class Pserial(serializers.ModelSerializer):
     class Meta:
        
         model=Product
         fields=('pname','slug','desc','price','images','stock','avail','category')