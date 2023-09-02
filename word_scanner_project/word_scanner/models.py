# word_scanner/models.py

from django.db import models
from django.contrib.auth.models import User

class ScannedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

class Word(models.Model):
    article = models.ForeignKey(ScannedArticle, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
