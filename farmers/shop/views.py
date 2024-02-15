from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect,HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib import messages


# Create your views here.


def Location(req):
    return render(req, 'shop/location.html')

def searches(req):
    form = Search1()
    if req.method == 'GET':
        form = Search1(req.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            show_product = Course.objects.filter(name__icontains=search)
        else:
            show_product = []
    else:
        form = Search1()
        show_product = []
    return render(req,'show_product.html',{'show_product':show_product,'form':form})

def advice_view(req):
    return render(req, 'shop/advice.html')


def product(req):
    allproduct = AllProduct.objects.all()
    context = {'allproduct':allproduct}
    return render(req, 'shop/show_product.html',context)

@login_required
def Showdetall_product(req,product_id):
    one_product = AllProduct.objects.filter(id=product_id)
    context = {'product':one_product}
    return render(req, 'shop/showdetall_product.html',context)

def Buy_product(req):
    return render(req, 'shop/buy_product.html')

@login_required
# def Sell_product(req):
#     if req.method == 'POST':
#         form = UploadForm(req.POST)
#         if form.is_valid():
#                 form.save()
#         else:
#             print(form.errors.as_data())
                
           
#         return HttpResponseRedirect(reverse('show_product'))
    
#     form = UploadForm()
#     context = {'form': form}
#     return render(req, 'shop/sell_product.html', context)
def Sell_product(req):
    status = Status.objects.all()
    form = UploadForm()
    if req.method == 'POST':
        form = UploadForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_product')
    else:
        form = UploadForm()

    return render(req, 'shop/sell_product.html',{'form': form,'status':status})

def Basket(req):
    return render(req, 'shop/basket.html')
# def Showdetall_product(request, product_id):
#     allProduct_instance = get_object_or_404(AllProduct, id=product_id)
#     return render(request, 'shop/Showdetall_product.html', {'AllProduct': allProduct_instance})
    
def update(req,id):
    form = Update()
    c = AllProduct.objects.get(pk=id)
    if req.method == 'POST':
        form = Update(req.POST,instance=c)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Update(instance=c)

    return render(req,'shop/edit_product.html',{'form':form})

# def delete_view(req,id):
#     s = AllProduct.objects.get(pk=id)
#     s.delete()
#     return redirect('delete_view')

