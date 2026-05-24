import secrets
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from newuser.models import Newuser
from newuser.forms import NewuserRegisterForm, ProfileUpdateForm
from config.settings import EMAIL_HOST_USER
from django.shortcuts import redirect
from django.urls import reverse


class NewuserCreateView(CreateView):
    model = Newuser
    form_class = NewuserRegisterForm
    success_url = reverse_lazy("newuser:login")


    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/newuser/email-confirm/{token}/"
        send_mail(
            subject="Добро пожаловать",
            message=f"Спасибо за регистрацию! {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(Newuser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("newuser:login"))


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Newuser
    form_class = ProfileUpdateForm
    template_name = "newuser/profile_update.html"
    success_url = reverse_lazy("profile")


    def get_object(self):
        return self.request.user
