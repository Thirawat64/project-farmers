from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

@login_required
def Location(req):
    return render(req, 'shop/location.html')

def searches(request):
    form = Search1()
    if request.method == 'GET':
        form = Search1(request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            result = Course.objects.filter(name__icontains=search)
        else:
            result = []
    else:
        form = Search1()
        result = []
    return render(request,'location.html',{'result':result,'form':form})

def advice_view(req):
    return render(req, 'shop/advice.html')

def product(req):
    allproduct = AllProduct.objects.all()
    comtext = {'allproduct':allproduct}
    return render(req, 'shop/show_product.html',comtext)

#def delete_view(req,id):
    s = AllProduct.objects.get(pk=id)
    s.delete()
    return redirect('delete_view')