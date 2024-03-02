from rest_framework import serializers

from .models import Customer


class Cserial(serializers.ModelSerializer):
     class Meta:
        
        model=Customer
        fields=('mail','phone','addedat','add1')
        

