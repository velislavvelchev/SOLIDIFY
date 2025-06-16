from django.urls import path
from SOLIDIFY.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]