from django.db import models
from django.contrib.auth.models import User


SUCCESS = 1
PENDING = 2
CANCEL = 3
ORDER_STATUS_CHOICES = (
        (SUCCESS, 'Success'),
        (PENDING, 'Pending order'),
        (CANCEL, 'cancel order')
)

    
class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)
     updated_on = models.DateTimeField(auto_now=True)
     class Meta:
         abstract = True

class Category(TimeStampedModel):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Products(TimeStampedModel):  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=60) 
    price = models.IntegerField(default=0)
    brand = models.CharField(max_length=60)
    image = models.ImageField(upload_to = "images/")
    in_stock = models.BooleanField(default = True)
    
    def __str__(self):
        return '{} {}'.format(self.product_name, self.id)


class Cart(TimeStampedModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField(default=0)
    cart_status = models.IntegerField(default = 2,choices = ORDER_STATUS_CHOICES) 
    is_active = models.BooleanField(default = True)
    def __str__(self):
        return '{} {}'.format(self.products,self.user)
        
        
    def get_total_products_price(self):
        return self.quantity * self.price 


class Wishlist(TimeStampedModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    price = models.IntegerField()


class Order(TimeStampedModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.ManyToManyField(Cart)
    order_status = models.IntegerField(default = 1,choices = ORDER_STATUS_CHOICES) 
    tax =  models.FloatField(default = 0.1)
    status = models.BooleanField(default = False)


class payment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE,null = True)
    paid_user = models.ForeignKey(Order, on_delete = models.CASCADE)
    transaction_id = models.TextField(max_length=200)
    paid_status =  models.IntegerField(default = 2,choices = ORDER_STATUS_CHOICES)
    amount = models.IntegerField()
    email = models.EmailField()
  
 
    
