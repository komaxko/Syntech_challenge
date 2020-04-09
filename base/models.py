import uuid

from django.db import models

__all__ = (
    'EditorAbstractModel',
    'TimeStampedAbstractModel'
)


class TimeStampedAbstractModel(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    class Meta:
        abstract = True


class EditorAbstractModel(models.Model):
    created_by = models.UUIDField()
    modified_by = models.UUIDField()

    class Meta:
        abstract = True
