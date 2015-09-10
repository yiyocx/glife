# coding=utf-8
from rest_framework import authentication, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import UserSerializer

from models import User


class ListUsers(generics.ListCreateAPIView):
    """
    Lista todos los usuarios del sistema

    * Requiere autenticación por Token
    * Solo los usuarios administrativos pueden acceder a esta vista
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAdminUser, )