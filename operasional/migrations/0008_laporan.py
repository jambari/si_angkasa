# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tata_usaha', '0007_auto_20160728_2051'),
        ('operasional', '0007_magnetbumi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laporan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=200)),
                ('batas_waktu', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('penyusun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tata_usaha.Pegawai')),
            ],
            options={
                'ordering': ['batas_waktu'],
                'verbose_name_plural': 'Laporan',
            },
        ),
    ]
