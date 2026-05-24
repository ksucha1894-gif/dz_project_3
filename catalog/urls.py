from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    HomeTemplateView,
    ContactsTemplateView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsByCategoryView,
)


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("catalog/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("category/<int:category_id>/", ProductsByCategoryView.as_view(), name="products_by_category"),
]
