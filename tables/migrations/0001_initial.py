# Generated by Django 2.2.6 on 2020-04-09 20:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('created_by', models.UUIDField()),
                ('modified_by', models.UUIDField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('number', models.SmallIntegerField()),
                ('seats', models.SmallIntegerField()),
                ('shape', models.SmallIntegerField(choices=[(1, 'RECTANGULAR'), (2, 'OVAL')])),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('size', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
            options={
                'verbose_name': 'Table',
                'verbose_name_plural': 'Tables',
                'db_table': 'tables',
                'ordering': ['number', 'seats'],
            },
        ),
    ]