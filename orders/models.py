from django.db import models

from base.models import (UUIDAbstractModel,TimeStampedAbstractModel, EditorAbstractModel)
from tables.models import Table


class Order(UUIDAbstractModel,TimeStampedAbstractModel, EditorAbstractModel):
    # allow unregistered users create objects
    created_by = models.UUIDField(null=True, blank=True)
    modified_by = models.UUIDField(null=True, blank=True)

    is_deleted = models.BooleanField(default=False)
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(null=False, blank=False)
    name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    email_send = models.BooleanField(default=False)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['date', 'confirmed']

    def __str__(self):
        return f'{self.name}'
