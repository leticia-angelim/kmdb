from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from .permissions import IsAdminOrCreateOnly
from .serializers import UserSerializer
from .models import User


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreateOnly]

    serializer_class = UserSerializer
    queryset = User.objects.all()
