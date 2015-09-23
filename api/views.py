# coding=utf-8
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, generics
from rest_framework import filters

from api.filters import DocumentFilter
from api.permissions import IsOwnerOrReadOnly, UserPermission
from api.serializers import UserSerializer, TagSerializer, DocumentSerializer
from models import Document, Tag

User = get_user_model()

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


class UserListView(generics.ListAPIView):
    """
    Permite que los usuarios autenticados puedan ver el listado de usuarios existentes
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalle de un usuario
    Un usuario solo puede editar y eliminar su propia información.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, UserPermission,)
