from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from royalapi.models import Product, ProductType
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status


class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for products"""
    class Meta:
        model = Product
        fields = ('title', 'price', 'in_stock', 'type_id')
        depth = 1

class Products(ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        try:
            product_type = ProductType.objects.get(pk=request.data['type_id'])
            new_product = Product.objects.create(
                title = request.data['title'],
                price = request.data['price'],
                in_stock = True,
                type_id = product_type
            )
            serializer = ProductSerializer(
            new_product, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)