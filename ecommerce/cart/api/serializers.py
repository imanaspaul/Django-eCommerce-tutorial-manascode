from rest_framework import serializers
from products.models import Product
from cart.models import Cart, Order

# Cart Serializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        read_only = ['created']

# Order Serializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only = ['created']
