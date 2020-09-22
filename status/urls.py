from os import name
from django.urls import path

from .views import StatusAPIView, StatusAPIDetailView


urlpatterns = [
    path('status/', StatusAPIView.as_view(), name='list'),
    path('status/<id>/', StatusAPIDetailView.as_view(), name='detail'),
]