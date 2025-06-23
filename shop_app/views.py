from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductModelForm


def index(request):
    return render(request, 'shop_app/base.html')


class ProductListView(ListView):
    model = Product
    template_name = 'shop_app/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop_app/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop_app/create_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'shop_app/edit_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop_app/delete_product'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')


from django.shortcuts import render
