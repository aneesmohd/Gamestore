from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from store.models import Product, Cart,Wishlist

@login_required(login_url="loginpage")
def index(request):
    wishlist= Wishlist.objects.filter(user=request.user)
    context= {"wishlist":wishlist}

    return render(request,"store/wishlist.html",context)



def add_to_wishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            try:
                product_check = Product.objects.get(id=prod_id)
            except Product.DoesNotExist:
                return JsonResponse({"status": "No such product found"})

            if Wishlist.objects.filter(user=request.user, product=product_check).exists():
                return JsonResponse({"status": "Already in wishlist"})
            else:
                Wishlist.objects.create(user=request.user, product=product_check)
                return JsonResponse({"status": "Added to wishlist"})
        else:
            return JsonResponse({"status": "Login required"})
    return redirect("/")


def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            try:
                wishlist_item = Wishlist.objects.get(user=request.user, product_id=prod_id)
                wishlist_item.delete()
                return JsonResponse({'status': 'Product removed from wishlist'})
            except Wishlist.DoesNotExist:
                return JsonResponse({'status': 'Product not found in wishlist'})
        else:
            return JsonResponse({'status': 'Login to continue'})
    return redirect('/')