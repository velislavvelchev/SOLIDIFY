from django.urls import path

from SOLIDIFY.categories.views import CreateCategoryView

urlpatterns = [
    path('create/', CreateCategoryView.as_view(), name='create-category'),
]