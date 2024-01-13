from django.urls import path
from .views import (PostList, PostDetail, PostSearch, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate,
   ArticlesUpdate, ArticlesDelete, CategoryListView, subscribe
)
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', cache_page(60*1)(PostList.as_view()), name='post_list'),
   path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
   path('news/search/', cache_page(60*5)(PostSearch.as_view()), name='post_detail'),
   path('news/create/', cache_page(60*5)(NewsCreate.as_view()), name='news_create'),
   path('news/<int:pk>/edit/', cache_page(60*5)(NewsUpdate.as_view()), name='news_update'),
   path('news/<int:pk>/delete/', cache_page(60*5)(NewsDelete.as_view()), name='news_delete'),
   path('articles/create/', cache_page(60*5)(ArticlesCreate.as_view()), name='articles_create'),
   path('articles/<int:pk>/edit/', cache_page(60*5)(ArticlesUpdate.as_view()), name='articles_update'),
   path('articles/<int:pk>/delete/', cache_page(60*5)(ArticlesDelete.as_view()), name='articles_delete'),
   path('categories/<int:pk>', cache_page(60*5)(CategoryListView.as_view()), name='category_list'),
   path('categories/<int:pk>/subscribe', cache_page(60*5)(subscribe), name='subscribe')
]