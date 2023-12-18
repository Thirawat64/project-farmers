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
            show_product = Course.objects.filter(name__icontains=search)
        else:
            show_product = []
    else:
        form = Search1()
        show_product = []
    return render(request,'show_product.html',{'show_product':show_product,'form':form})

def advice_view(req):
    return render(req, 'shop/advice.html')

def product(req):
    allproduct = AllProduct.objects.all()
    context = {'allproduct':allproduct}
    return render(req, 'shop/show_product.html',context)

def Showdetall_product(req,allproduct_id):
    one_product = AllProduct.objects.get(id=allproduct_id)
    context = {'product':one_product}
    return render(req, 'shop/showdetall_product.html',context)
    


#def delete_view(req,id):
    s = AllProduct.objects.get(pk=id)
    s.delete()
    return redirect('delete_view')