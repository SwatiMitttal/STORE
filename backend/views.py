from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse


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

