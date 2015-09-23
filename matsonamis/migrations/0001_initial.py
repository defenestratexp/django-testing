# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ami',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ami_name', models.CharField(default='Empty', max_length=25)),
                ('ami_id', models.CharField(max_length=12)),
                ('ami_creation_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystemVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_version', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='OpSysPurpose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_purpose_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='operatingsystem',
            name='os_sys_version',
            field=models.ForeignKey(to='matsonamis.OperatingSystemVersion'),
        ),
        migrations.AddField(
            model_name='ami',
            name='ami_os_system',
            field=models.ForeignKey(to='matsonamis.OperatingSystem'),
        ),
        migrations.AddField(
            model_name='ami',
            name='ami_os_version',
            field=models.ForeignKey(to='matsonamis.OperatingSystemVersion'),
        ),
        migrations.AddField(
            model_name='ami',
            name='ami_purpose',
            field=models.ForeignKey(to='matsonamis.OpSysPurpose'),
        ),
    ]
