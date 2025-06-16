from django.urls import path

from SOLIDIFY.accounts.views import UserRegisterView

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),
]