from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from tata_usaha.models import *
# Create your models here.

class Gempabumi(models.Model):
    """(Gempabumi description)"""
    tanggal = models.DateField(default=datetime.datetime.today)
    origin_time = models.TimeField(blank=True)
    lintang = models.FloatField()
    bujur = models.FloatField()
    kedalaman = models.PositiveIntegerField(blank=True, null=True)
    magnitudo = models.FloatField()
    remark = models.CharField(blank=True, max_length=200)
    terasa = models.BooleanField(default=False)
    pga_z = models.FloatField(default = 0)
    pga_ns = models.FloatField(default = 0)
    pga_ew = models.FloatField(default = 0)
    shakemap = models.BooleanField(default=False)
    observer = models.ForeignKey(User)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Gempabumi'

    def __str__(self):
        return str(self.tanggal)+" "+ str(self.origin_time)

    def __unicode__(self):
        return str(self.tanggal)+" "+ str(self.origin_time)


class ListrikUdara(models.Model):
    """(ListrikUdara description)"""
    tanggal = models.DateField(default=datetime.datetime.today)
    stroke = models.IntegerField(blank=True, null=True, default=0)
    apm_stroke = models.FloatField(default=0.0, verbose_name = 'average')
    strong = models.IntegerField(blank=True, null=True, default=0)
    apm_strong = models.FloatField(default=0.0, verbose_name = 'average')
    noise = models.IntegerField(blank=True, null=True, default=0)
    apm_noise = models.FloatField(default=0.0, verbose_name = 'average')
    energy = models.IntegerField(blank=True, null=True, default=0)
    apm_energy = models.FloatField(default=0.0, verbose_name = 'average')
    stroke_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_stroke_peak = models.TimeField(blank=True, default='00:00:00')
    strong_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_strong_peak = models.TimeField(blank=True, default='00:00:00')
    noise_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_noise_peak = models.TimeField(blank=True, default='00:00:00')
    energy_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_energy_peak = models.TimeField(blank=True, default='00:00:00')
    energy_ratio_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_ratio_peak = models.TimeField(blank=True, default='00:00:00')
    signal_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_signal_peak = models.TimeField(blank=True, default='00:00:00')
    observer = models.ForeignKey(User)

    def __str__(self):
        return str(self.tanggal)


    def __unicode__(self):
        return u"ListrikUdara"

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Listrik Udara'


class Hujan(models.Model):
    """(Hujan description)"""
    KATEGORI_CHOICES = (
        ('nihil', 'Nihil'),
        ('sangat ringan','Sangat Ringan'),
        ('ringan', 'ringan'),
        ('sedang', 'Sedang'),
        ('lebat', 'Lebat'),
        ('sangat lebat', 'sangat lebat'),
    )

    tanggal = models.DateField(default=datetime.datetime.today)
    jumlah = models.FloatField(default=0.0)
    keterangan = models.CharField(blank=True, max_length=100, choices = KATEGORI_CHOICES)
    observer = models.ForeignKey(User)

    def __str__(self):
        return str(self.tanggal)

    def __unicode__(self):
        return str(self.tanggal)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Hujan'


class Magnetbumi(models.Model):
    KOMPONEN_CHOICES = (
        ('X', 'X'),
        ('Y', 'Y'),
        ('Z', 'Z'),
        ('H', 'H'),
        ('D', 'D'),
        ('I', 'I'),
        ('F', 'F'),
    )

    tanggal = models.DateField(default=datetime.datetime.today)
    komponen = models.CharField(blank=True, max_length=2, choices = KOMPONEN_CHOICES)
    jam00 = models.FloatField(default = 0.00, verbose_name='00-01')
    jam01 = models.FloatField(default = 0.00, verbose_name='01-02')
    jam02 = models.FloatField(default = 0.00, verbose_name='02-03')
    jam03 = models.FloatField(default = 0.00, verbose_name='03-04')
    jam04 = models.FloatField(default = 0.00, verbose_name='04-05')
    jam05 = models.FloatField(default = 0.00, verbose_name='05-06')
    jam06 = models.FloatField(default = 0.00, verbose_name='06-07')
    jam07 = models.FloatField(default = 0.00, verbose_name='07-08')
    jam08 = models.FloatField(default = 0.00, verbose_name='08-09')
    jam09 = models.FloatField(default = 0.00, verbose_name='09-10')
    jam10 = models.FloatField(default = 0.00, verbose_name='10-11')
    jam11 = models.FloatField(default = 0.00, verbose_name='11-12')
    jam12 = models.FloatField(default = 0.00, verbose_name='12-13')
    jam13 = models.FloatField(default = 0.00, verbose_name='13-14')
    jam14 = models.FloatField(default = 0.00, verbose_name='14-15')
    jam15 = models.FloatField(default = 0.00, verbose_name='15-16')
    jam16 = models.FloatField(default = 0.00, verbose_name='16-17')
    jam17 = models.FloatField(default = 0.00, verbose_name='17-18')
    jam18 = models.FloatField(default = 0.00, verbose_name='18-19')
    jam19 = models.FloatField(default = 0.00, verbose_name='19-20')
    jam20 = models.FloatField(default = 0.00, verbose_name='20-21')
    jam21 = models.FloatField(default = 0.00, verbose_name='21-22')
    jam22 = models.FloatField(default = 0.00, verbose_name='22-23')
    jam23 = models.FloatField(default = 0.00, verbose_name='23-00')
    rata_rata = models.FloatField(default = 0.00)

    def __str__(self):
        return str(self.tanggal)

    def __unicode__(self):
        return self.tanggal

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Magnetbumi'


class Laporan(models.Model):
    """(Laporan description)"""
    nama = models.CharField(blank=True, max_length=200)
    batas_waktu = models.DateField()
    penyusun = models.ForeignKey(Pegawai)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

    def __unicode__(self):
        return self.nama

    class Meta:
        ordering = ['batas_waktu']
        verbose_name_plural = 'Laporan'
