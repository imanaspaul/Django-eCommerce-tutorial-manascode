from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from cart.api.serializers import CartSerializer,OrderSerializer
from cart.models import Cart,Order


class CartAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class OrderAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
