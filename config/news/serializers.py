from rest_framework import serializers
from .models import NewsPost

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ['id', 'title', 'slug', 'image', 'excerpt', 'content', 'published_date']