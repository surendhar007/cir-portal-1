# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20160610_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='AptitudeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='EligibilityTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='HRTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='QuantatitiveTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='ReasoningTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='VerbalTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
    ]
