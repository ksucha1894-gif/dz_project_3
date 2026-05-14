from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (
    HomeTemplateView,
    ContactsTemplateView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
