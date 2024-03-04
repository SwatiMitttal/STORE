from django.shortcuts import render
from django.http import HttpResponse
from .form import RForm
# Create your views here.



def login(req):
    return HttpResponse('LOGIGN')

def logout(req):
    return HttpResponse('LOGOUT')
def signup(req):
    form=RForm()
    context={
        'form':form
    }
    return render(req,'register.html',context)