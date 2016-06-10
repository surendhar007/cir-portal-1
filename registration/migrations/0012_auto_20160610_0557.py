# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='Test Name')),
                ('date', models.DateField(verbose_name='Test Date')),
                ('type', models.CharField(max_length=20, verbose_name='Test Type', choices=[(b'Technical', 'Technical'), (b'HR', 'HR'), (b'Quantitative', 'Quantitative'), (b'Verbals', 'Verbals'), (b'Reasoning', 'Reasoning'), (b'Eligibility', 'Eligibility'), (b'Aptitude', 'Aptitude')])),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='stud_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='aums_id',
            field=models.CharField(max_length=32, unique=True, serialize=False, verbose_name='Aums ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.FloatField(null=True, verbose_name='CGPA', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_arrears',
            field=models.FloatField(null=True, verbose_name='No of current arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist_arrears',
            field=models.FloatField(null=True, verbose_name='No of history arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s1',
            field=models.FloatField(null=True, verbose_name='S1 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s2',
            field=models.FloatField(null=True, verbose_name='S2 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s3',
            field=models.FloatField(null=True, verbose_name='S3 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s4',
            field=models.FloatField(null=True, verbose_name='S4 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s5',
            field=models.FloatField(null=True, verbose_name='S5 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s6',
            field=models.FloatField(null=True, verbose_name='S6 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.FloatField(null=True, verbose_name='10th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.FloatField(null=True, verbose_name='12th Mark', blank=True),
        ),
    ]
