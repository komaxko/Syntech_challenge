from .models import Order
from base.serializers import (ChoicesField, FilteredListSerializer)
from base.exceptions import AlreadyExists
from rest_framework import serializers
from datetime import timedelta
from django.core.mail import send_mail


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = Order
        read_only_fields = ('id', 'confirmed')
        exclude = ('created_by', 'created', 'modified_by', 'is_deleted', 'email_send')

    def create(self, validated_data):

        # It might done better with some timedelta of 45 mins for example
        # e.g. reservation A has a table 1 for 19:00
        # and reservation B could be booked for 19:01
        # and a confirmation from stuff bust be done before email been sent
        # & emails could be send via service workers asynchronously

        if not Order.objects.filter(table=validated_data.get('table'),
                                    date=validated_data.get('date')):
            obj = Order.objects.create(**validated_data)
            send_mail(
                subject='Table reservation',
                message='Your reservation has been confirmed, ...some info & ads ...',
                from_email='sender@example.com',
                recipient_list=['receiver1@example.com']
            )

            return obj
        else:
            raise AlreadyExists('Sorry, this table is reserved for this date!')

    def update(self, instance, validated_data):
        instance.save()
        return instance