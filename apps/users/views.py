
from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.users.models import User
from .serializers import UserRegistrationSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
