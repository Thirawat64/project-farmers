from audioop import reverse
from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from user.forms import  RegisterForm

# Create your views here.
def Register(req:HttpRequest):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return HttpResponseRedirect(reverse("main:home"))
    else:
        form = RegisterForm()
         
    context = {"form": form}
    return render(req, 'users/register.html',context)
#password non12345678

def Login(req):
    return render(req, 'registration/login.html')