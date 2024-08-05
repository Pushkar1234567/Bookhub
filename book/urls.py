from django.urls import path
from .views import fetch_books, BookRecommendationListCreate, BookRecommendationDetail, LikeListCreate, CommentListCreate

urlpatterns = [
    path('search/', fetch_books, name='fetch_books'),
    path('recommendations/', BookRecommendationListCreate.as_view(), name='recommendation_list_create'),
    path('recommendations/<int:pk>/', BookRecommendationDetail.as_view(), name='recommendation_detail'),
    path('likes/', LikeListCreate.as_view(), name='like_list_create'),
    path('comments/', CommentListCreate.as_view(), name='comment_list_create'),
]