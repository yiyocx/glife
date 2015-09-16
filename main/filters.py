import django_filters

from main.models import Tag, Document


class DocumentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        to_field_name='name',
        conjoined=True
    )

    class Meta:
        model = Document
        fields = ('title', 'description', 'tags')
