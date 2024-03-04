from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registerr(req):
    
    return render(req,'register.html')

def login(req):
    return HttpResponse('LOGIGN')

def logout(req):
    return HttpResponse('LOGOUT')
def signup(req):
    return HttpResponse('SIGNUP')