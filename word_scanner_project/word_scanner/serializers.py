# word_scanner/serializers.py
from rest_framework import serializers
from .models import ScannedArticle, Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class ScannedArticleSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = ScannedArticle
        fields = '__all__'
