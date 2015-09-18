# coding=utf-8
from rest_framework import permissions, generics, viewsets
from rest_framework import filters

from api.filters import DocumentFilter
from api.permissions import IsOwnerOrReadOnly
from api.serializers import UserSerializer, TagSerializer, DocumentSerializer
from custom_auth.models import User
from models import Document, Tag


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

    def perform_create(self, serializer):
        data = serializer.validated_data
        # del data['confirm_password']

        print('la data es %s' % data)
        serializer.save(**data)
        super(ListUsers, self).perform_create(serializer)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Recurso User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer