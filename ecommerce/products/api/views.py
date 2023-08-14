from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.api.serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category


class ProductAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
