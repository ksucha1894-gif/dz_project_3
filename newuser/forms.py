from django.contrib.auth.forms import UserCreationForm
from django import forms
from newuser.models import Newuser


class NewuserRegisterForm(UserCreationForm):
    class Meta:
        model = Newuser
        fields = ("email", "password1", "password2")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Newuser
        fields = ["email", "avatar", "phone", "country"]
