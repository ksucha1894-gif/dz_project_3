from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_product_from_cache():
    """Получает данные по продуктам из кэша. Если кэш пуст - получает данные из БД."""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)
