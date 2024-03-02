from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import Customer
from .serializers import Cserial
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def hello(req):
    return render(req,'hello.html')
def home(req):
    return render(req,'page2.html')
def aboutus(req):
    return render(req,'aboutus.html')

@csrf_exempt
def cview(req):
    
    custs=Customer.objects.all()
    ss=Cserial(custs,many=True)
    
    
    return JsonResponse(ss.data,safe=False)
