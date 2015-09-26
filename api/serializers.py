from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Document, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(many=True, view_name='document-detail', read_only=True)
    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('url', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth',
                  'is_active', 'documents')
        read_only_fields = ('is_active',)


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    tags = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='name')

    class Meta:
        model = Document
        fields = ('url', 'file', 'title', 'description', 'owner', 'tags', 'votes', 'created_at', 'updated_at')


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Token del rest_framework.authtoken
    """

    class Meta:
        model = Token
        fields = ('key',)
