from django.contrib.auth.models import AbstractUser
from django.db import models


class Newuser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="newuser/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    country = models.TextField(
        max_length=100, verbose_name="Страна", help_text="Введите страну проживания"
    )

    token = models.CharField(
        max_length=100,
        verbose_name="Токен",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
