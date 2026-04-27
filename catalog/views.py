from gettext import Catalog

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from catalog.models import Product


class HomeTemplateView(TemplateView):
    model = Product
    template_name = "product/home.html"


class ContactsTemplateView(TemplateView):
    model = Product
    template_name = "product/contacts.html"


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"

    # app_name/<model_name>_<action>
    # catalog/product_list.html


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"


# def home(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "home.html")
#
#
# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         message = request.POST.get("message")
#
#         return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
#     return render(request, "contacts.html")
#
#
# def product_list(request):
#     products = Product.objects.all()
#     context = {"object_list": products}
#     return render(request, 'product_list.html', context)
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)
