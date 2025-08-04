from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from store.models import Product, Cart

@login_required
def addtocart(request):
    if request.method == "POST":
        try:
            prod_id = int(request.POST.get('product_id'))
            prod_qty = int(request.POST.get('product_qty'))

            product = Product.objects.get(id=prod_id)

            if product.quantity < prod_qty:
                return JsonResponse({'status': f"Only {product.quantity} in stock"})

            # Check if already added
            existing_cart = Cart.objects.filter(user=request.user, product_id=prod_id).first()
            if existing_cart:
                return JsonResponse({'status': "Product already in cart"})

            # Add to cart
            Cart.objects.create(
                user=request.user,
                product=product,
                product_qty=prod_qty
            )

            return JsonResponse({'status': "Product added to cart successfully"})

        except Product.DoesNotExist:
            return JsonResponse({'status': "No such product found"})
        except Exception as e:
            return JsonResponse({'status': f"Error: {str(e)}"})

    return JsonResponse({'status': "Invalid request"})


def viewcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        context ={'cart':cart}
        return render(request,"store/cart.html",context)
    else:
        return redirect('loginpage')


def updatecart(request):
    if request.method=="POST":
        prod_id=int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart= Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({"status":'update successfully'})
    return redirect("/")


def deletecartitem(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem=Cart.objects.get(product_id= prod_id,user=request.user)
            cartitem.delete()
            return JsonResponse({"status":"Delete successfully"})
    return redirect("/")





