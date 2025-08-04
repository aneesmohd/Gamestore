from webbrowser import register

from django.urls import path
from . import  views
from store.controller import authview, cart, checkout,order
from .controller import wishlist

urlpatterns = [
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<slug:slug>/', views.collectionsview, name='collectionsview'),
    path('collections/<slug:cate_slug>/<slug:prod_slug>/', views.productview, name='productview'),

    path('register/',authview.register,name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path("logout/",authview.logoutpage,name="logout"),

    path("add-to-cart/", cart.addtocart, name="addtocart"),
    path("cart",cart.viewcart,name='cart'),
    path("update-cart",cart.updatecart,name="updatecart"),
    path("delete-cart-item",cart.deletecartitem,name="delete-cart-item"),

    path("wishlist/", wishlist.index, name="wishlist"),
    path("add-to-wishlist/", wishlist.add_to_wishlist, name="add-to-wishlist"),
    path("delete-wishlist-item/", wishlist.deletewishlistitem, name='delete_wishlist_item'),

    path("checkout",checkout.index,name='checkout'),
    path("place-order",checkout.placeorder,name='placeorder'),
    path("razorpaycheck/", checkout.razorpaycheck, name="razorpaycheck"),

    path("order/", order.order_view, name='order'),
    path("view-order/<str:t_no>/",order.view_order,name='orderview')

]