# coding=utf-8
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, generics
from rest_framework import filters

from api.filters import DocumentFilter
from api.permissions import IsOwnerOrReadOnly, UserPermission, IsAdminOrReadOnly
from api.serializers import UserSerializer, TagSerializer, DocumentSerializer
from models import Document, Tag

User = get_user_model()


class TagListView(generics.ListCreateAPIView):
    """
    Permite crear nuevos tags y listar los tags existentes.

    El usuario debe estar autenticado
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalle de un Tag que permite visualizar, actualizar y eliminar información.

    * Los usuarios autenticados solo pueden visualizar información de un Tag
    * Los usuarios administradores pueden actualizar y eliminar información de un Tag
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly,)


class DocumentViewSet(viewsets.ModelViewSet):
    """
    Permite crear, listar, obtener, actualizar y eliminar documentos

    * Los usuarios autenticados pueden crear documentos, listarlos y ver el detalle de cualquiera
    * Un documento solo puede ser actualizado y eliminado por su propietario o por un Administrador
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    filter_class = DocumentFilter
    search_fields = ('title', 'description', 'tags__name')
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserListView(generics.ListAPIView):
    """
    Permite listar los usuarios existentes.

    El usuario debe estar autenticado
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalle de un Usuario que permite visualizar, actualizar y eliminar información.

    * Requiere autenticación
    * Un usuario pueden visualizar la información de cualquier Usuario
    * Un usuario solo puede editar y eliminar su propia información.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, UserPermission,)
