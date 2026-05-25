from gettext import Catalog

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden

from catalog.models import Product
from catalog.forms import ProductForm, ProductModeratorForm

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.services import get_product_from_cache, get_products_by_category
from django.shortcuts import render


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "object_list"


    def get_queryset(self):
        return get_product_from_cache()


class ProductsByCategoryView(ListView):
    model = Product
    template_name = "product/products_by_category.html"
    context_object_name = "object_list"


    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return get_products_by_category(category_id)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "object"

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.has_perm("catalog.can_unpublish_product",
                                                                                "catalog.can_delete_product"):
            return self.object
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_list.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm(
            "catalog.can_delete_product"
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.has_perm("catalog.can_unpublish_product",
                                                                                "catalog.can_delete_product"):
            return self.object
        raise PermissionDenied


class HomeTemplateView(TemplateView):
    model = Product
    template_name = "product/home.html"


class ContactsTemplateView(TemplateView):
    model = Product
    template_name = "product/contacts.html"
