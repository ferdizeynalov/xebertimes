from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news'),
    path('<slug:category_slug>/<int:news_id>', views.news_detail, name='news_detail'),
    path('categories/<slug:category_slug>', views.news_by_category, name='news_by_category'),
    path('search/', views.search, name='search'),
]
