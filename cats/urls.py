from django.urls import path

from cats.apps import CatsConfig
from cats.views import CategoriesListView, CatsListView, CatCreateView, CatUpdateView, CatDeleteView, IndexView, \
    AllCatsListView

app_name = CatsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/ ', CategoriesListView.as_view(), name='categories'),
    path('cats/<int:pk>/', CatsListView.as_view(), name='cats'),
    path('all_cats/', AllCatsListView.as_view(), name='all_cats'),
    path('cats/create/', CatCreateView.as_view(), name='cat_create'),
    path('cats/<int:pk>/update/', CatUpdateView.as_view(), name='cat_update'),
    path('cats/delete/<int:pk>/', CatDeleteView.as_view(), name='cat_confirm_delete'),

]