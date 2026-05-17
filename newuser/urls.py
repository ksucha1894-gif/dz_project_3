from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from newuser.apps import NewuserConfig
from newuser.views import NewuserCreateView, email_verification

app_name = NewuserConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", NewuserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
