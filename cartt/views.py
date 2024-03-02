from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from .models import Cartt,Cartitem
import numpy as np
from django.conf import settings
def cidd(req):
    cart=req.session.session_key
    if not cart:
        cart=req.session.create()
    return cart

def add_cart(req,pid):
    
    prod=Product.objects.get(id=pid)
    try:
        cartt=Cartt.objects.get(ccd=cidd(req))
    except Cartt.DoesNotExist:
        cartt=Cartt.objects.create(ccd=cidd(req))
    cartt.save()
    
    try:
        citem=Cartitem.objects.get(product=prod,cart=cartt)
        citem.quantity+=1
       
        if prod.stock==1:
            prod.avail=False
        prod.stock-=1
            
    except Cartitem.DoesNotExist:
       citem=Cartitem.objects.create(
           product=prod,
            cart=cartt,
            quantity=1
        )
    citem.save()
    context={
        
        'citem':citem
    }
    
    return redirect('cart')

def rem_cart(req,pid):
    cart=Cartt.objects.get(ccd=cidd(req))  
    prod=get_object_or_404(Product,id=pid) 
    citem=get_object_or_404(Cartitem,cart=cart,product=prod)
    
    if citem.quantity>1:
        citem.quantity-=1
        citem.save()
    else:
        citem.delete()
    return redirect('cart');

def cart(req,quantity=0,tot=0):
    try:
        cart=Cartt.objects.get(ccd=cidd(req))
        citems=Cartitem.objects.filter(cart=cart,is_alive=True)
        
        for item in citems:
             quantity+=item.quantity
             tot+= item.product.price * item.quantity
        taxx=(tot*2)/100
        gtot=tot+taxx  
        
    except :
        pass
    ind=np.arange(1,len(citems))
    context={
        'gtotal':gtot,
        'taxx':taxx,
        'total':tot,
        'quantity':quantity,
        'cart':cart,
        'ind':ind,
        'citems':citems
    }
    
    return render(req,'cart.html',context)
    
    
    