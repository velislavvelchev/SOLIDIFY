from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'common/home.html'

class DopamineView(TemplateView):
    template_name = 'common/dopamine.html'
