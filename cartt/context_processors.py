from .models import Cartt,Cartitem
from . import views
from django.contrib import admin

def counter(req):
    if 'admin' in req.path:
        return {}
    sid=views.cidd(req)
    ccount=0
    try:
        cart=Cartt.objects.get(ccd=sid)
        citems=Cartitem.objects.all().filter(cart=cart)
        
        for item in citems:
            
            ccount+=item.quantity
    except Cartt.DoesNotExist:
        ccount=0
       
    return dict({'cc':ccount})