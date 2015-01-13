# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=3, choices=[(b'Mr', b'Mr'), (b'Ms', b'Ms'), (b'Miss', b'Miss'), (b'Mrs', b'Mrs')])),
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('job', models.ForeignKey(to='staff.Job')),
            ],
            options={
                'verbose_name_plural': 'staff',
            },
            bases=(models.Model,),
        ),
    ]
