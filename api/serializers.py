from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers

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


def validate_password(self, password):
    print('Hola %s %s' % (self, password))


class UserSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(many=True, view_name='document-detail', read_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('url', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth',
                  'password', 'confirm_password', 'is_active', 'documents')
        read_only_fields = ('is_active', )
        #exclude = ('groups', 'user_permissions', )

    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password == confirm_password:
            del attrs['confirm_password']
            return attrs
        raise ValidationError('Password and confirm password must be the same')






