from django.shortcuts import render

# Create your views here.
def Register(req):
    return render(req, 'user/register.html')

def Login(req):
    return render(req, 'user/login.html')