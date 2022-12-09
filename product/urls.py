from django.urls import path,include
from product.views import(
    LoginView,
    RegisterUserAPIView,
    Checkout_Sessionview,
    webhook_endpoint,
    #CartView,
)
from product import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'category', views.CategoryView)
router.register(r'product', views.ProductView)
router.register(r'cart', views.CartView)
router.register(r'wish',views.WishlistView)
router.register(r'order',views.OrderView)
router.register(r'payment',views.PaymentView)




urlpatterns = [
     path('', include(router.urls)),
     path('login/', LoginView.as_view()),
     path('register/',RegisterUserAPIView.as_view()),
     path('checkout/',Checkout_Sessionview.as_view()),
     path('web/',webhook_endpoint.as_view()),
     #path('cart/',CartView.as_view()),
]