# coding=utf-8
from rest_framework import permissions, generics, viewsets
from rest_framework import filters

from main.filters import DocumentFilter
from main.permissions import IsOwnerOrReadOnly
from main.serializers import UserSerializer, TagSerializer, DocumentSerializer
from models import User, Document, Tag


class TagViewSet(viewsets.ModelViewSet):
    """Recurso Tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """Recurso Document"""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend, )
    filter_class = DocumentFilter
    search_fields = ('title', 'description', 'tags__name')
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListUsers(generics.CreateAPIView):
    """
    Lista todos los usuarios del sistema

    * Requiere autenticación por Token
    * Solo los usuarios administrativos pueden acceder a esta vista
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Recurso User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer