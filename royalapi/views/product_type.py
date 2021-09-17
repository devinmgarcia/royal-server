from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from royalapi.models import ProductType
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status


class ProductTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for productTypes"""
    class Meta:
        model = ProductType
        fields = ('id', 'name')
        depth = 1

class ProductTypesView(ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        product_types = ProductType.objects.all()
        serializer = ProductTypeSerializer(
            product_types, many=True, context={'request': request})
        return Response(serializer.data)
