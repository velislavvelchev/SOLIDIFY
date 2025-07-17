from django.urls import path, include
from SOLIDIFY.common.views import HomePageView, DopamineView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('learn/', include([
        path('dopamine/', DopamineView.as_view(), name='dopamine')
    ]))
]