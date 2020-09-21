from os import name
from django.urls import path

from .views import StatusAPIView


urlpatterns = [
    path('status/', StatusAPIView.as_view(), name='list'),
    path('status/', StatusCreateAPIView.as_view(), name='create'),
    path('status/<id>/', StatusDetailAPIView.as_view(), name='detail'),
    path('status/<id>/', StatusUpdateAPIView.as_view(), name='update'),
    path('status/<id>/', StatusDeleteAPIView.as_view(), name='delete')
]