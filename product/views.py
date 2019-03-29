from django.shortcuts import render, redirect

# other
from django.urls import reverse
# own
from .form import productCreateForm
from .models import Product

# Create your views here.
def productListView(request,*args,**kwargs):
    queryset = Product.objects.all()
    
    
    context = {
        "queryset": queryset
    }
    return render(request,"product/product_list.html",context)


def productDetailView(request,id):
    obj = Product.objects.get(id=id)
    context = {
         "product": obj
     }
    return render(request,'product/product_detail.html',context)



def productCreateView(request, *args,**kwargs):
    form = productCreateForm(request.POST or None )
    if form.is_valid():
        form.save()
        form = productCreateForm()
    context = {
        "create_form": form
    }

    return render(request,'product/product_create.html',context)

def productEditView(request, id):
    obj = Product.objects.get(id=id)
    form = productCreateForm(request.POST or None, instance = obj)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            form = productCreateForm()
    context = {
        "edit_form": form,
        "product_id": id
    }
    return render(request,'product/product_edit.html',context)


def productDeleteView(request, id):
    obj = Product.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/", {
            "message": "Product deleted"
        })
    context = {
        "product": obj
    }
    return render(request,'product/product_delete.html',context)