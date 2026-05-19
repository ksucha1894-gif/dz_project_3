from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование продукта"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Прикрепите изображение продукта"}
        )
        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите категорию продукта"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )

    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "").lower()
        description = cleaned_data.get("description", "").lower()

        for word in self.forbidden_words:
            if word in name or word in description:
                raise ValidationError(
                    f"Название и описание не должны содержать запрещенные слова: {word}"
                )

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной!")
        return price


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ("name", "publish")
