from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from .permissions import IsAdminOrReadOnly
from .serializers import MovieSerializer
from .models import Movie


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
