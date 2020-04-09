from django.contrib.postgres.fields import ArrayField
from django.db import models
from enum import IntEnum

from base.models import (TimeStampedAbstractModel, EditorAbstractModel)


class Shape(IntEnum):
    RECTANGULAR = 1
    OVAL = 2


class Table(TimeStampedAbstractModel, EditorAbstractModel):
    is_deleted = models.BooleanField(default=False)
    number = models.SmallIntegerField(null=False, blank=False)
    seats = models.SmallIntegerField(null=False, blank=False)
    shape = models.SmallIntegerField(null=False, blank=False, choices=[(item.value, item.name) for item in Shape])
    coordinates = ArrayField(null=False, blank=False, base_field=models.IntegerField())
    size = ArrayField(null=False, blank=False, base_field=models.IntegerField())

    class Meta:
        db_table = 'tables'
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
        ordering = ['number', 'seats']

    def __str__(self):
        return f'{self.number}'

    @staticmethod
    def get_last_order(report_id):
        table = Table.objects.filter(is_deleted=False).order_by('number').last()
        if not table:
            return 1
        return table.order + 1