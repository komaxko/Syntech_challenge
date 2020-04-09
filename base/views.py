import logging

from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action


class BaseViewSet(viewsets.ModelViewSet):
    logger = logging.getLogger('challenge.logging')

    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (AllowAny,)
    serializer_class = None
    queryset = None

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_field)
        is_staff = self.request.user.is_staff
        if pk:
            return get_object_or_404(self.queryset, pk=pk)
        return self.queryset.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset())
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = request.user.pk
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=user, modified_by=user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_queryset()
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(modified_by=request.user.id)
            return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        self.perform_destroy(instance, request.user.id)
        return Response('', status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance, user):
        instance.is_deleted = True
        instance.modified_by = user
        return instance.save()

    @action(detail=False, methods=['post'])
    def bulk_delete(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        queryset = self.get_queryset().filter(id__in=ids)
        queryset.update(is_deleted=True, modified_by=request.user.pk)
        return Response('', status.HTTP_204_NO_CONTENT)