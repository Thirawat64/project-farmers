from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect,HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib import messages





def Location(req):
    return render(req, 'shop/location.html')

def searches(req):
    form = Search1()
    if req.method == 'POST':
        form = Search1(req.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search is not None:
                show_product = AllProduct.objects.filter(product_location__icontains=search) or AllProduct.objects.filter(product_name__icontains=search)
           
            for i in show_product:
                print(i)
        else:
            show_product = AllProduct.objects.all()
    else:
        form = Search1()
        # show_product = []
    return render(req,'shop/show_product_search.html',{'show_product':show_product,'form':form})

def advice_view(req):
    return render(req, 'shop/advice.html')


# def product(req):
#     allproduct = AllProduct.objects.all()
#     context = {'allproduct':allproduct}
#     return render(req, 'shop/show_product.html',context)

def product(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        # กรองข้อมูลตามคำค้นหา
        allproduct = AllProduct.objects.filter(product_name__icontains=search_query)
    else:
        # ถ้าไม่มีการส่งคำค้นหามา
        allproduct = AllProduct.objects.all()

    context = {'allproduct': allproduct}
    return render(request, 'shop/show_product.html', context)

@login_required
def Showdetall_product(req,product_id):
    one_product = AllProduct.objects.get(pk=product_id)
    context = {'product':one_product}
    return render(req, 'shop/showdetall_product.html',context)

def Buy_product(req):
    return render(req, 'shop/buy_product.html')

@login_required

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

# def Basket(req):
#     return render(req, 'shop/basket.html')

    
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

def delete(req, id):
    print(id)
    CartItem.objects.get(pk=id).delete()
    return redirect('cart')

def add_to_cart(req, product_id):
    product = AllProduct.objects.get(pk=product_id)  # ดึงสินค้าจากฐานข้อมูลด้วย ID
    cart = Cart.objects.get(user=req.user)
    
    cart_item = CartItem.objects.filter(cart=cart, product=product ,user=req.user)
    if cart_item:
        for i in cart_item:
            if i.product.id == product_id:
                i.quantity += 1
                i.save()
    else:
        cart_items = CartItem.objects.create(cart=cart, product=product ,user=req.user)
        cart_items.save()

    return redirect('cart')  # ส่งไปยังหน้าตะกร้าสินค้า

def cart(req):
    Cart = CartItem.objects.filter(user=req.user)
    context = {'Cart':Cart}
    return render(req,'shop/cart.html',context)

def buy_product(req):
    return render(req, 'shop/buy_product.html')