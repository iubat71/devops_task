

from itertools import product
from statistics import quantiles
from unicodedata import category
from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.db.models import Sum

from .ProductForm import ProductrefillForm
from .PackageForm import PackagerefillForm
from .models import *
from app import PackageForm



def home(request):
    pr=Package.objects.all()
    
    con={
        'r':pr
    }    
    return render(request,'index.html',con)


def product_refill(request):
  
    productrefill=ProductrefillForm()
    if request.method=='POST':
        f=ProductrefillForm(request.POST)
        f.save()
        return HttpResponse("save")
    con={
        'ps':productrefill,
        # 'p':c
    }
 
    return render(request,'product.html',con)  




def p_refill(request):
    # p_fill=Package.objects.all()
    packageform=PackagerefillForm()
    if request.method=='POST':
        f=PackagerefillForm(request.POST)
        f.save()
        return HttpResponse("save")
    


    
    con={
        'ps':packageform,
        # 'total':p_fill
    }


    return render(request,'package_refill.html',con)  
    

def package(request):
    pr=Package_refill.objects.filter(status="Activated")
    con={
        'pr':pr
    }
    
    return render(request,'packages.html',con)


def card(request):
    pr=Package_refill.objects.all()
    con={
        'pr':pr
    }
    return render(request,'card.html',con)    


def update_view(request, pk):
    id = get_object_or_404(Product_refill, pk=pk)
    form = ProductrefillForm(instance=id)
    if request.method == 'POST':
        form = ProductrefillForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('update', pk=pk)
    return render(request, 'product.html', {'form': form})


def load_product(request):
    c_id = request.GET.get('id')
    prd= Product_refill.objects.filter(product_id=c_id)
    con={'prs': prd}
    return render(request, 'pr.html', con)   



def pupdate_view(request, pk):
    id = get_object_or_404(Package_refill, pk=pk)
    form = PackagerefillForm(instance=id)
    if request.method == 'POST':
        form = PackagerefillForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('pupdate', pk=pk)
    return render(request, 'package_refill.html', {'form': form})


def load_package(request):
    id = request.GET.get('id')
    packd= Package_refill.objects.filter(package_id=id)
    con={'p': packd}
    return render(request, 'pack.html', con)  
  