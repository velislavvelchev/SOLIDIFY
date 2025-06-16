from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from SOLIDIFY.accounts.forms import AppUserForm


# Create your views here.
class UserRegisterView(CreateView):
    form_class = AppUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')