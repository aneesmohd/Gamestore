from tkinter.constants import CASCADE
from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def get_file_path(request,filename):
    original_filename = filename
    nowTime=datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename='%s%s' % (nowTime,original_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug = models.CharField(max_length=100,null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to= get_file_path,null=False,blank=False)
    description = models.TextField(max_length=600,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    meta_title = models.CharField(max_length=100,null=False,blank=False)
    meta_keyword = models.CharField(max_length=100,null=False,blank=False)
    meta_description = models.CharField(max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    category= models.ForeignKey(Category,on_delete= models.CASCADE)
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    small_description = models.CharField(max_length=300, null=False, blank=False)
    quantity =models.IntegerField(null=False,blank=False)
    description =models.TextField(max_length=600, null=False, blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    tag = models.CharField(max_length=20,null=False,blank=False)
    meta_title = models.CharField(max_length=50, null=False, blank=False)
    meta_keyword = models.CharField(max_length=50, null=False, blank=False)
    meta_description = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at=models.DateTimeField(auto_now_add=True)

# class UserDetails(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     email=models.EmailField()
#     phone=models.CharField(max_length=15)
#     address=models.TextField()
#     city=models.CharField(max_length=100)
#     state=models.CharField(max_length=100)
#     country=models.CharField(max_length=100)
#     pincode=models.CharField(max_length=6)
#     total_price=models.FloatField()
#     payment_mode=models.CharField(max_length=50)
#     status=models.CharField(max_length=100, default="Pending")
#     created_at=models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.id} | {self.user.username} | {self.status}'
# class OrderItem(models.Model):
#     order=models.ForeignKey(UserDetails, on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     price=models.FloatField()
#     quantity=models.IntegerField()
#
#     def __str__(self):
#         return f"{self.order.id} - {self.product.name}"
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=25,null=False)
    lname=models.CharField(max_length=20,null=False)
    email=models.CharField(max_length=20,null=False)
    phone=models.CharField(max_length=15,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=10,null=False)
    state=models.CharField(max_length=10,null=False)
    country=models.CharField(max_length=15,null=False)
    pincode=models.CharField(max_length=15,null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=20,null=False)
    payment_id=models.CharField(max_length=20,null=False)

    orderstatus ={
        ("Pending","Pending"),
        ("Out for shipping","Out for shipping"),
        ("Completed","Completed"),
    }
    status=models.CharField(max_length=20,choices=orderstatus,default="Pending")
    message=models.TextField(null=False)
    tracking_no=models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return f"{self.order.user.username} - {self.product.name}"


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=50,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=50,null=False)
    state=models.CharField(max_length=50,null=False)
    country=models.CharField(max_length=50,null=False)
    pincode=models.CharField(max_length=50,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"





