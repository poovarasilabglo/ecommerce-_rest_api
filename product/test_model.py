from django.test import TestCase
from product.models import Cart, Category,Products,User


class CategoryTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        
        self.category1 = Category.objects.create(name ='mobile')
        self.category2 = Category.objects.create(name = 'labtop')

    def test_str(self):
        self.assertEqual(str(self.category1),'mobile')
        self.assertEqual(str(self.category2),'labtop')


class ProductsTestCase(TestCase):
    def setUp(self):
        super().setUp()
        
        self.category = Category.objects.create(name = 'mobile')
        self.product = Products.objects.create(category =self.category,product_name ='bike', id = 4)

    def test_str(self):
        self.assertEqual(str(self.product),'bike 4')  


class CartTestCase(TestCase):
    def setUp(self):
        super().setUp()
        
        user = User(username="username", email="example@gmail.com")
        user.set_password("password2@")
        user.save()
        self.category = Category.objects.create(name = 'mobile')
        self.product = Products.objects.create(category =self.category,product_name ='bike', id = 4)
        self.carts = Cart(user = user,
                                 products =self.product,
                                 quantity= 2,
                                 price= 50,
                                 cart_status= 2,
                                 is_active =True)
    
    def test_str(self):
        self.assertEqual(str(self.carts),'bike 4 username')

        
