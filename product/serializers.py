from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from product.models import(
    Category,
    Products,
    Cart,
    Wishlist,
    payment,
    Order,
)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = self.authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField('get_user_token')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name', 'token')
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
        }
 
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
 
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url','id', 'name','created_on',]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'product_name', 'price', 'brand', 'image', 'in_stock','category','created_on','updated_on']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    #products= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product')
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Cart
        fields = ['user', 'id', 'products', 'quantity','is_active','created_on','updated_on']


class WishlistSerializer(serializers.ModelSerializer):
     class Meta:
        model = Wishlist
        fields = ['user', 'product','created_on',]

class OrderSerializer(serializers.ModelSerializer):
     class Meta:
        model = Order
        fields = '__all__'


class paymentSerializer(serializers.ModelSerializer):
     user = serializers.ReadOnlyField(source='user.username')
     class Meta:
        model = payment
        fields = ['paid_user','transaction_id','paid_status','amount','email','user']




