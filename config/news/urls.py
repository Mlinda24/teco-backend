from django.urls import path
from .views import NewsPostList, NewsPostDetail

urlpatterns = [
    path('news/', NewsPostList.as_view(), name='news-list'),
    path('news/<slug:slug>/', NewsPostDetail.as_view(), name='news-detail'),
]