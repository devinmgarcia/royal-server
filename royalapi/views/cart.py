from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from royalapi.models import Cart, Customer, Product, CartProduct
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action

class CartSerializer(serializers.ModelSerializer):
    """JSON serializer for carts"""
    # products = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ('customer_id', 'order_complete', 'products')
        depth = 2

class CartView(ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def list(self, request):
        customer = Customer.objects.get(user=request.auth.user)
        cart = Cart.objects.get(customer_id=customer.id)
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
                cart = Cart.objects.get(customer_id=customer.id)
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
                cart = Cart.objects.get(customer_id=customer.id)
                cart_product = CartProduct.objects.filter(cart_id=cart.id, product_id=pk)
                cart_product.delete()
                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except Exception as ex:
                return Response({'message': ex.args[0]})
        