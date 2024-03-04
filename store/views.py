from django.shortcuts import render,get_object_or_404
from django.http.response import JsonResponse,HttpResponse,FileResponse
from django.http.request import HttpRequest
#from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import os
# Create your views here.
from django.core.paginator import Paginator
from  endless_pagination import utils
from django.db.models import Q

    
def store(req,cslug):
    from .models import Product,Category
    cats=None
    prods=None
    
    
   
        
    cat=Category.objects.filter(slug=cslug)
    prods=Product.objects.all().filter(category=cat[0],avail=True)
    pcount=prods.count()
    paginator=Paginator(prods,1)
    page=req.GET.get('page')
    pprods=paginator.get_page(page)
    
    context={
        'prods':pprods,
        #'pcount':pprods.count()
        
    }
    
    return render(req,'page2.html',context)
    

def pdetail(req,cslug,pslug):
    from .models import Product,Category
    cats=None
    prods=None
    
    prods=Product.objects.all().filter(slug=pslug)
    context={
        'prods':prods,
        'pcount':prods.count()
    }
    return render(req,'page2.html',context)

def search(req):
    from .models import Product
    kword=req.GET.get('kword')
    if kword:
        prods=Product.objects.order_by('price').filter(Q(desc__icontains=kword)| Q(pname__icontains=kword) )
    pcount=prods.count()
    context={
        'prods':prods,
        'pcount':pcount,
        'kword':kword
    }
    return render(req,'page2.html',context)

