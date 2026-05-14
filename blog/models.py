from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, verbose_name="Превью(изображение)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_sign = models.BooleanField(
        default=True, verbose_name="Признак публикации"
    )
    view_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["created_at", "name"]

    def __str__(self):
        return self.name
