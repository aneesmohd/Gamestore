# from Tools.scripts.patchcheck import status
# from Tools.scripts.patchcheck import status
# from Tools.scripts.patchcheck import status
from django.http import JsonResponse
from django.shortcuts import render, redirect
from unicodedata import category
from django.contrib import messages
from store.controller import cart

from store.models import Category, Product,Wishlist


# Create your views here.
def home(request):
    trending_products=Product.objects.filter(trending=1)
    context={"trending_products":trending_products}

    return  render(request,"store/home.html",context)

def collections(request):
    category =Category.objects.filter(status =0)
    context = {'category':category}
    return render(request,"store/collections.html",context)


def collectionsview(request,slug):
    if Category.objects.filter(slug=slug, status=0).exists():
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.get(slug=slug)
        context = {
            'products': products,
            'category': category
        }
        return render(request,'store/products/home.html', context)
    else:
        messages.warning(request, "No Such Category Found")
        return redirect("collections")


def productview(request,cate_slug,prod_slug):
    if Category.objects.filter(slug=cate_slug,status=0).exists():
        if Product.objects.filter(slug=prod_slug,status=0).exists():
            products =Product.objects.filter(slug=prod_slug,status=0).first()
            context={'products':products}
        else:
            messages.error(request,"no such product found")
            return redirect('collections')

    else:
        messages.error(request,'no such category found')
        return redirect("collections")
    return render(request,'store/products/view.html',context)

# def add_to_wishlist(request):
#     if request.method=="POST":
#         if request.user.is_authenticated:
#             prod_id=int(request.POST.get('product_id'))
#             product=Product.objects.get(id=prod_id)
#             if Wishlist.objects.filter(user=request.user,product=product).exists():
#                 return  JsonResponse({"status":"already in wish list"})
#             else:
#                 Wishlist.objects.create(user=request.user,product=product)
#                 return JsonResponse({"status":"added to wishlist"})
#         else:
#             return JsonResponse({"status":"Login required"})
#     return JsonResponse({"status":"Invalid request"})
