from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings
from rest_framework.reverse import reverse_lazy

from .forms import ContactUsForm
from .utils import EmailThread
from decouple import config

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'common/home.html'

class DopamineView(TemplateView):
    template_name = 'common/dopamine.html'

class AboutUsView(TemplateView):
    template_name = "common/about_us.html"


class ContactUsView(FormView):
    template_name = "common/contact_us.html"
    form_class = ContactUsForm
    success_url = reverse_lazy('contact-us')

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        if user.is_authenticated and hasattr(user, "profile"):
            profile = user.profile
            if profile.first_name and profile.last_name:
                initial['full_name'] = f"{profile.first_name} {profile.last_name}"
            initial['email'] = user.email
        return initial

    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['email']

        message += f"\n\n\nSend by {full_name}, {from_email}"

        EmailThread(
            subject,
            message,
            from_email,
            [settings.EMAIL_HOST_USER]
        ).start()

        messages.success(self.request, "Your email has been sent successfully!")
        return super().form_valid(form)