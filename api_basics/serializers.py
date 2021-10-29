from rest_framework import serializers
from .models import Article
from api_basics import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
