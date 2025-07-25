from django.urls import path, include
from SOLIDIFY.common.views import HomePageView, DopamineView, AboutUsView, ContactUsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('learn/', include([
        path('dopamine/', DopamineView.as_view(), name='dopamine'),
        path('about-us/', AboutUsView.as_view(), name='about-us'),
        path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    ]))
]