from django.urls import path 
from . views import checkout, payment, charge, oderView

app_name = "checkout"

urlpatterns = [
	path('checkout/', checkout, name="index"),
	path('payment/', payment, name="payment"),
	path('charge/', charge, name="charge"),
	path('my-orders/', oderView, name="oderView")
]