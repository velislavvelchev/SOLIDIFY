from django.urls import path
from SOLIDIFY.categories.views import CreateCategoryView, ListCategoriesView

urlpatterns = [
    path('create/', CreateCategoryView.as_view(), name='create-category'),
    path('all-categories/', ListCategoriesView.as_view(), name='all-categories'),
]