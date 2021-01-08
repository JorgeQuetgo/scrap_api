from rest_framework.response import Response

from rest_framework import viewsets, status
from api.models import Product
from api.serializers import ProductSerializer, PageScrapSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class PageScrappingViewSet(viewsets.ViewSet):
    serializer_class = PageScrapSerializer

    @staticmethod
    def create(request):
        serializer = PageScrapSerializer(data=request.data)
        if serializer.is_valid():
            result =serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=201)
