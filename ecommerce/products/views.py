from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Product
    template_name = 'products/home.html'


class ProductDetail(LoginRequiredMixin, DetailView):
	model = Product

	