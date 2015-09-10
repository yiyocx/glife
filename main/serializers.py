from rest_framework import serializers
from models import Tag, User


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'slug')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(many=True, view_name='document-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'documents')
