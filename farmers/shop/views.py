from django.shortcuts import render

# Create your views here.
def Location(req):
    return render(req, 'shop/location.html')