from rest_framework import generics, status
from users import serializers
# from survey_authentication.models import User
from rest_framework import permissions
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model

from users import permissions
from users.models import User

# UserModel = get_user_model()

class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated )
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsOwnerOrReadOnly, IsAuthenticated )
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

