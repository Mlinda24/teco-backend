from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import NewsPost
from .serializers import NewsPostSerializer

# API for listing all news (read-only)
class NewsPostList(generics.ListAPIView):
    queryset = NewsPost.objects.filter(is_published=True).order_by('-published_date')
    serializer_class = NewsPostSerializer

# API for fetching a single news article by slug (read-only)
class NewsPostDetail(generics.RetrieveAPIView):
    queryset = NewsPost.objects.filter(is_published=True)
    serializer_class = NewsPostSerializer
    lookup_field = 'slug'