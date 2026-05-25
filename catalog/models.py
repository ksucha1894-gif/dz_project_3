from django.db import models

from newuser.models import Newuser


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    owner = models.ForeignKey(
        Newuser,
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    publish = models.BooleanField(
        verbose_name="Дата публикации", default=False, blank=False
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]

    def __str__(self):
        return self.name
