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

    def retrieve(self, request, pk=None):
  
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        # get the product
        product = Product.objects.get(pk=pk)
        # set the products new values
        product.title = request.data["title"]
        product.price = request.data["price"]
        product.in_stock = request.data["in_stock"]
        # get the product type object
        product_type = ProductType.objects.get(pk=request.data['type_id'])
        # set the product type value
        product.type_id = product_type
        # save changes
        product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
    
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)