# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operasional', '0006_hujan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magnetbumi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(default=datetime.datetime.today)),
                ('komponen', models.CharField(blank=True, choices=[('X', 'X'), ('Y', 'Y'), ('Z', 'Z'), ('H', 'H'), ('D', 'D'), ('I', 'I'), ('F', 'F')], max_length=2)),
                ('jam00', models.FloatField(default=0.0, verbose_name='00-01')),
                ('jam01', models.FloatField(default=0.0, verbose_name='01-02')),
                ('jam02', models.FloatField(default=0.0, verbose_name='02-03')),
                ('jam03', models.FloatField(default=0.0, verbose_name='03-04')),
                ('jam04', models.FloatField(default=0.0, verbose_name='04-05')),
                ('jam05', models.FloatField(default=0.0, verbose_name='05-06')),
                ('jam06', models.FloatField(default=0.0, verbose_name='06-07')),
                ('jam07', models.FloatField(default=0.0, verbose_name='07-08')),
                ('jam08', models.FloatField(default=0.0, verbose_name='08-09')),
                ('jam09', models.FloatField(default=0.0, verbose_name='09-10')),
                ('jam10', models.FloatField(default=0.0, verbose_name='10-11')),
                ('jam11', models.FloatField(default=0.0, verbose_name='11-12')),
                ('jam12', models.FloatField(default=0.0, verbose_name='12-13')),
                ('jam13', models.FloatField(default=0.0, verbose_name='13-14')),
                ('jam14', models.FloatField(default=0.0, verbose_name='14-15')),
                ('jam15', models.FloatField(default=0.0, verbose_name='15-16')),
                ('jam16', models.FloatField(default=0.0, verbose_name='16-17')),
                ('jam17', models.FloatField(default=0.0, verbose_name='17-18')),
                ('jam18', models.FloatField(default=0.0, verbose_name='18-19')),
                ('jam19', models.FloatField(default=0.0, verbose_name='19-20')),
                ('jam20', models.FloatField(default=0.0, verbose_name='20-21')),
                ('jam21', models.FloatField(default=0.0, verbose_name='21-22')),
                ('jam22', models.FloatField(default=0.0, verbose_name='22-23')),
                ('jam23', models.FloatField(default=0.0, verbose_name='23-00')),
                ('rata_rata', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ['tanggal'],
                'verbose_name_plural': 'Magnetbumi',
            },
        ),
    ]