from django.contrib import admin
from product.models import(
     Category,
     Products,
     Cart,
     Wishlist,
     Order,
     payment,
)


class Categoryadmin(admin.ModelAdmin):
    list_display = ('id','name',)
admin.site.register(Category,Categoryadmin) 


class Productsadmin(admin.ModelAdmin):
    list_display = ('id','category','product_name','price','brand','image',)
admin.site.register(Products,Productsadmin) 


class Cartadmin(admin.ModelAdmin):
     list_display = ('id','user','price','products','quantity','cart_status')
admin.site.register(Cart,Cartadmin) 


class Orderadmin(admin.ModelAdmin):
     list_display = ('id','user','order_status')
admin.site.register(Order,Orderadmin)

admin.site.register(Wishlist)
admin.site.register(payment)


