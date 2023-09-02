# word_scanner/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_article, name='scan_article'),
]
