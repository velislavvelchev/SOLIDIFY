from django.contrib.auth.views import LoginView
from django.urls import path

from SOLIDIFY.accounts.views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]