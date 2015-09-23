# coding=utf-8
from django.contrib.auth import get_user_model, logout
from rest_framework import permissions, viewsets, generics, status, mixins, authentication
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
