from django.contrib.auth.views import LogoutView
from django.urls import path, include

from SOLIDIFY.accounts.views import UserRegisterView, UserLoginView, ProfileDetailsView, ProfileEditView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
    ]))
]