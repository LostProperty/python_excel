# -*- coding: utf-8 -*-
# Technique from http://stackoverflow.com/questions/25960850/loading-initial-data-with-django-1-7-and-data-migrations
import os

from django.db import migrations
from django.core import serializers


fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.yaml'


def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)
    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('yaml', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this models..."
    Staff = apps.get_model("staff", "Staff")
    Staff.objects.all().delete()
    Job = apps.get_model("staff", "Job")
    Job.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
