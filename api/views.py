# coding=utf-8
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView
from rest_framework import permissions, viewsets, generics, status
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.filters import DocumentFilter
from api.models import DocumentVote
from api.permissions import IsOwnerOrReadOnly, UserPermission, IsAdminOrReadOnly
from api.serializers import UserSerializer, TagSerializer, DocumentSerializer
from models import Document, Tag

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'


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


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upvote_document(request, pk):
    """
    Permite votar positivamente (upvote) un Documento

    :param pk: id del documento al que se le hace upvote
    """

    try:
        document = Document.objects.get(pk=pk)
    except ObjectDoesNotExist as e:
        return Response(data={'error': e.message}, status=status.HTTP_404_NOT_FOUND)

    votes_queryset = DocumentVote.objects.filter(document=document, owner=request.user)
    if votes_queryset.exists():
        current_vote = votes_queryset[0]
        if current_vote.is_upvote:
            # Si el usuario que realiza la petición intenta hacer upvote nuevamente
            # a este documento se elimina la votación que tiene actualmente
            current_vote.delete()
        else:
            # Si la votación actual es downvote entonces se cambia su estado a upvote
            current_vote.is_upvote = True
            current_vote.save()
        return Response(status=status.HTTP_200_OK)
    else:
        vote = DocumentVote(document=document, owner=request.user, is_upvote=True)
        vote.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def downvote_document(request, pk):
    """
    Permite votar negativamente (downvote) un Documento

    :param pk: id del documento al que se le hace downvote
    """

    try:
        document = Document.objects.get(pk=pk)
    except ObjectDoesNotExist as e:
        return Response(data={'error': e.message}, status=status.HTTP_404_NOT_FOUND)

    votes_queryset = DocumentVote.objects.filter(document=document, owner=request.user)
    if votes_queryset.exists():
        current_vote = votes_queryset[0]
        if current_vote.is_upvote:
            # Si la votación actual es upvote entonces se cambia su estado a downvote
            current_vote.is_upvote = False
            current_vote.save()
        else:
            # Si el usuario que realiza la petición intenta hacer downvote nuevamente
            # a este documento se elimina la votación que tiene actualmente
            current_vote.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        vote = DocumentVote(document=document, owner=request.user, is_upvote=False)
        vote.save()
        return Response(status=status.HTTP_200_OK)
