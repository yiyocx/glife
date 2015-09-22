from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Document, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Tag


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tags = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='name')

    class Meta:
        model = Document


class UserSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(many=True, view_name='document-detail', read_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('url', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth',
                  'password', 'is_active', 'documents')
        read_only_fields = ('is_active',)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data['email'], validated_data['first_name'],
                                                    validated_data['last_name'], validated_data['password'])
        user.phone_number = validated_data['phone_number']
        user.date_of_birth = validated_data['date_of_birth']
        return user


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Token del rest_framework.authtoken
    """

    class Meta:
        model = Token
        fields = ('key',)
