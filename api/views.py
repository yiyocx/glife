# coding=utf-8
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, generics, status
from rest_framework import filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.filters import DocumentFilter
from api.permissions import IsOwnerOrReadOnly, UserPermission
from api.serializers import UserSerializer, TagSerializer, DocumentSerializer, TokenSerializer
from models import Document, Tag


class TagViewSet(viewsets.ModelViewSet):
    """Recurso Tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """Recurso Document"""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    filter_class = DocumentFilter
    search_fields = ('title', 'description', 'tags__name')
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)


class RegisterView(generics.CreateAPIView):
    """
    Crea un nuevo usuario en caso de que el usuario no exista actualmente.
    Retorna un Token en caso de registro exitoso.

    Acepta los siguientes parametros obligatorios POST: email, first_name, last_name, password.
    Opcionalmente puede recibir: phone_number, date_of_birth
    """

    serializer_class = TokenSerializer
    permission_classes = (permissions.AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', )

    def post(self, request, *args, **kwargs):
        user_created = get_user_model().objects.create_user(**request.data)
        token, created = Token.objects.get_or_create(user=user_created)

        serializer = self.get_serializer(instance=token, data={'key': token.key})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
