from django.urls import path
from .views import ExtractorsListApiView

urlpatterns = [
    path('', ExtractorsListApiView.as_view()),
]
