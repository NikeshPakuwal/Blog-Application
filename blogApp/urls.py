from blogApp.models import Category
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdateProfileView, DeletePostView, AddCategoryView, CategoryView, CategoryListView


urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),

    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>', UpdateProfileView.as_view(), name = 'update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name = 'delete_post'),

    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),

]