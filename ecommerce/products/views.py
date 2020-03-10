from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .filters import ProductFilter
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Product
    template_name = 'products/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

def home(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'products/home.html', {'filter': product_filter})

class ProductDetail(LoginRequiredMixin, DetailView):
	model = Product

	