from django.contrib.auth.forms import UserCreationForm

from newuser.models import Newuser


class NewuserRegisterForm(UserCreationForm):
    class Meta:
        model = Newuser
        fields = ("email", "password1", "password2")
