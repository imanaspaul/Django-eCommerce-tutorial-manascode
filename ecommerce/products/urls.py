from django.urls import path, include
from rest_framework.routers import SimpleRouter
from cart.views import add_to_cart, remove_from_cart, CartView, decreaseCart
from . views import home, ProductDetail, Home
from products.api.views import *

app_name= 'mainapp'

router = SimpleRouter()
router.register('api/products', ProductAPIView)
router.register('api/category', CategoryAPIView)


urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', include(router.urls)),
    path('', home, name='home'),
    path('p', Home.as_view(), name='home'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]