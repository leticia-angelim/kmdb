from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import generics

from movies.models import Movie
from .permissions import IsAdminOrIsCriticOrReadOnly
from .serializers import ReviewSerializer
from .models import Review


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrIsCriticOrReadOnly]

    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = get_object_or_404(Movie, pk=self.kwargs["movie_id"])

        return Review.objects.filter(movie_id=movie.id)

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs["movie_id"])

        serializer.save(movie_id=movie.id, critic=self.request.user)
