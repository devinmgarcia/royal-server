from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from royalapi.models import ProductImage
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

class ProductImageView(ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def destroy(self, request, pk=None):

        product_image = ProductImage.objects.get(pk=pk)
        product_image.delete()
      
        return Response({}, status=status.HTTP_204_NO_CONTENT)
