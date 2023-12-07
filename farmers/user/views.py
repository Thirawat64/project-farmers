from django.shortcuts import render

# Create your views here.
def Register(req):
    return render(req, 'registration/register.html')

def Login(req):
    return render(req, 'registration/login.html')