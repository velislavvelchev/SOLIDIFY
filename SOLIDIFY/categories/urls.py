from django.urls import path, include
from SOLIDIFY.categories.views import CreateCategoryView, ListCategoriesView, EditCategoryView, DetailsCategoryView

urlpatterns = [
    path('create/', CreateCategoryView.as_view(), name='create-category'),
    path('all-categories/', ListCategoriesView.as_view(), name='all-categories'),
    path('<int:pk>/', include([
        path('edit/', EditCategoryView.as_view(), name='edit-category'),
        path('details/', DetailsCategoryView.as_view(), name='details-category'),
    ]))
]