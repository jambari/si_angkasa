# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 03:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JenisAkun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_akun', models.CharField(choices=[('pegawai', 'Pegawai'), ('admin', 'admin')], max_length=50)),
                ('akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.TextField(blank=True)),
                ('nip', models.CharField(blank=True, max_length=100)),
                ('tempat_lahir', models.CharField(blank=True, max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('pangkat', models.CharField(blank=True, max_length=100)),
                ('golongan', models.CharField(blank=True, max_length=15)),
                ('pendidikan_terakhir', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nomor_rekening', models.CharField(blank=True, max_length=100)),
                ('agama', models.CharField(blank=True, choices=[('islam', 'Islam'), ('protestan', 'Protestan'), ('katolik', 'Katolik'), ('hindu', 'Hindu'), ('budha', 'Budha'), ('konghuchu', 'Konghuchu')], max_length=100)),
                ('status', models.CharField(blank=True, choices=[('pns', 'PNS'), ('cpns', 'CPNS'), ('honor', 'Honor'), ('magang', 'Magang')], max_length=100)),
                ('bagian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tata_usaha.Divisi')),
                ('jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tata_usaha.Jabatan')),
            ],
        ),
        migrations.AddField(
            model_name='jenisakun',
            name='pegawai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tata_usaha.Pegawai'),
        ),
    ]