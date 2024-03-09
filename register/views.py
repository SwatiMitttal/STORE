from django.shortcuts import render
from django.http import HttpResponse
from .form import RForm
from .models import Account,Manager
# Create your views here.



def login(req):
    return HttpResponse('LOGIGN')

def logout(req):
    return HttpResponse('LOGOUT')
def signup(req):
    if req.method=='POST':
        form=RForm(req.POST)
        if form.is_valid():
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            passw=form.cleaned_data['passw']
            uname=email.split('@')[0]
            user=Manager.create_user(fname,lname,email,passw)
    else:
        form=RForm()
    context={
        'form':form
    }
    return render(req,'register.html',context)