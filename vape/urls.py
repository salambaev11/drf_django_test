
from django.urls import path

from vape.views import (
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView, PostDeleteAPIView, )

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', PostUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteAPIView.as_view(), name='delete'),
]