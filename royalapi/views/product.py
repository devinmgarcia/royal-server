from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from royalapi.models import Product, ProductType, ProductImage, product_image
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.core.files.base import ContentFile
import base64
import uuid

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

class ProductsView(ViewSet):

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
                type = product_type
            )
            product_images = request.data['images']
            for image in product_images:
                format, imgstr = image.split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')
                ProductImage.objects.create(
                    image = data,
                    product = new_product
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
   
        product = Product.objects.get(pk=pk)
     
        product.title = request.data["title"]
        product.price = request.data["price"]
        # product.in_stock = request.data["in_stock"]
    
        product_type = ProductType.objects.get(pk=request.data['type_id'])
        product.type_id = product_type

        product_images = request.data['images']
        for image in product_images:
            format, imgstr = image.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')
            ProductImage.objects.create(
                image = data,
                product = product
            )
        
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