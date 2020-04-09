from .models import (Table, Shape)
from base.serializers import (ChoicesField, FilteredListSerializer)
from rest_framework import serializers


class TableSerializer(serializers.ModelSerializer):
    shape = ChoicesField(choices=[(item.value, item.name) for item in Shape])

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = Table
        read_only_fields = ('id',)
        exclude = ('created_by', 'created', 'modified_by', 'is_deleted')