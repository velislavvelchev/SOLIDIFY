from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from SOLIDIFY.accounts.forms import AppUserCreationForm, ProfileEditForm, AppUserLoginForm
from SOLIDIFY.accounts.models import Profile



class UserRegisterView(CreateView):
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    # Logic to log in the user directly after registration
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return response

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm



class ProfileDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk


class ProfileEditView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )

# redirect the user to django admin login if they make a logout request from the admin panel
def admin_logout_view(request):
    logout(request)
    referer = request.META.get('HTTP_REFERER', '')
    if '/admin' in referer:
        return redirect('/admin/login/')
    return redirect(reverse('login'))

# redirect to 403 if the user has no permissions
def permission_denied_view(request, exception=None):
    return render(request, '403.html', status=403)