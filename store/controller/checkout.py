import random

from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Product,Cart,Wishlist,Profile,Order,OrderItem
from django.http.response import JsonResponse
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User


def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)

    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    context = {'cartitems': cartitems, 'total_price': total_price}
    return render(request, "store/checkout.html", context)

@login_required(login_url="loginpage")
def placeorder(request):
    if request.method == "POST":
        currentuser=User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('firstname')
            currentuser.last_name=request.POST.get('lastname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user=request.user
            userprofile.phone = request.POST.get('phone')  # lowercase
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()

        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('firstname')
        neworder.lname = request.POST.get('lastname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')

        neworder.payment_mode=request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_mode')

        cart=Cart.objects.filter(user=request.user)
        cart_total_price=sum(item.product.selling_price * item.product_qty for item in cart)
        neworder.total_price=cart_total_price
        trackno="Anees"+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno).exists():
            trackno="Anees" +str(random.randint(1111111,9999999))

        neworder.tracking_no=trackno
        neworder.save()

        for item in cart:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )

            orderproduct=Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity -= item.product_qty
            orderproduct.save()

        Cart.objects.filter(user=request.user).delete()
        messages.success(request,"Your order has been placed successfully!")

        payMode=request.POST.get('payment_mode')
        if payMode == "Paid by Razorpay":
            return JsonResponse({'stats':'your order has been placed successfully!!!'})

    return redirect('order/')
@login_required(login_url="loginpage")

def razorpaycheck(request):
    cart=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cart:
        total_price +=item.product.selling_price * item.product_qty
    return JsonResponse({"total_price":total_price})




