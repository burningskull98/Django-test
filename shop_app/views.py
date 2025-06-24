"""
Этот модуль отвечает за обработку пользовательских запросов и отображение данных в приложении.
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Product
from .forms import ProductModelForm



def index(request):
    """
        Обрабатывает запросы к главной странице приложения.
        """
    return render(request, 'shop_app/base.html')


class ProductListView(ListView):
    """
       Представление для отображения списка продуктов.
      """
    model = Product
    template_name = 'shop_app/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    """
    Представление для отображения подробной информации о продукте.
   """
    model = Product
    template_name = 'shop_app/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    """
         Представление для создания продукта.
         """
    model = Product
    template_name = 'shop_app/create_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')


class ProductUpdateView(UpdateView):
    """
         Представление для редактирования продукта.
         """
    model = Product
    template_name = 'shop_app/edit_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')


class ProductDeleteView(DeleteView):
    """
     Представление для удаления продукта.
     """
    model = Product
    template_name = 'shop_app/delete_product'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')
