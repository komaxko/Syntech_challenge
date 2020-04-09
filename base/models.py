import uuid

from django.db import models

__all__ = (
    'EditorAbstractModel',
    'TimeStampedAbstractModel',
    'UUIDAbstractModel',
)


class UUIDAbstractModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


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
