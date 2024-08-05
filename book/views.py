from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
import requests
from django.http import JsonResponse
from .models import BookRecommendation, Like, Comment
from .serializers import BookRecommendationSerializer, LikeSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

def fetch_books(request):
    query = request.GET.get('q', '')
    api_key = settings.GOOGLE_BOOKS_API_KEY
    try:
        api_url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
        response = requests.get(api_url)
        if response.status_code == 200:
            return JsonResponse(response.json())
        return JsonResponse({'error': 'Failed to fetch data from Google Books API'}, status=500)
    except Exception as E:
        return {"message" : f"Error occured while fetching the data : {E}"} 


class BookRecommendationListCreate(APIView):

    def get(self, request):
        recommendations = BookRecommendation.objects.all()
        serializer = BookRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookRecommendationDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(BookRecommendation, pk=pk)

    def get(self, request, pk):
        recommendation = self.get_object(pk)
        serializer = BookRecommendationSerializer(recommendation)
        return Response(serializer.data)

    def put(self, request, pk):
        recommendation = self.get_object(pk)
        serializer = BookRecommendationSerializer(recommendation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recommendation = self.get_object(pk)
        recommendation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeListCreate(APIView):

    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentListCreate(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

