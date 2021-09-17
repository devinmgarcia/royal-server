from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from royalapi.models import Cart, Customer, Product, CartProduct,  ProductImage, customer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User

class ProductImageSerializer(serializers.ModelSerializer):
    """JSON serializer for products"""
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'product')

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for products"""
    productimage_set = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'in_stock', 'type', "productimage_set")
        depth = 1
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    user = UserSerializer(many=False)
    class Meta:
        model = Customer
        fields = ('id', 'user')

class CartSerializer(serializers.ModelSerializer):
    """JSON serializer for carts"""
    products = ProductSerializer(many=True)
    customer = CustomerSerializer(many=False)
    class Meta:
        model = Cart
        fields = ('id', 'customer', 'order_complete', 'products', 'total')
        depth = 3

class CartView(ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def list(self, request):
        customer = Customer.objects.get(user=request.auth.user)
        cart = Cart.objects.get(customer_id=customer.id, order_complete=False)
        serializer = CartSerializer(cart, many=False, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        try:
            customer = Customer.objects.get(user=request.auth.user)
            new_cart = Cart.objects.create(
                customer = customer,
                order_complete = False
            )
            return Response({}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post', 'delete'], detail=True)
    def edit(self, request, pk=None):

        if request.method == "POST":       
            try:
                customer = Customer.objects.get(user=request.auth.user)
                cart = Cart.objects.get(customer_id=customer.id, order_complete=False)
                product = Product.objects.get(pk=pk)
                CartProduct.objects.create(
                    cart = cart,
                    product = product
                )
                return Response({}, status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({'message': ex.args[0]})
        if request.method == "DELETE":       
            try:
                customer = Customer.objects.get(user=request.auth.user)
                cart = Cart.objects.get(customer_id=customer.id, order_complete=False)
                cart_product = CartProduct.objects.filter(cart_id=cart.id, product_id=pk)
                cart_product.delete()
                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except Exception as ex:
                return Response({'message': ex.args[0]})
        