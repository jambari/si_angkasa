from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from tata_usaha.models import *
from operasional.models import *
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def AtkView(request):
    atk = None
    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        atk = AlatTulisKantor.objects.filter(tanggal__year=tahun, tanggal__month=bulan).order_by(Coalesce('tanggal','nama_barang').asc())
    return render(request,'tata_usaha/atk.html', {"atk": atk} )


@login_required(login_url=settings.LOGIN_URL)
def DiklatView(request):
    diklat = Diklat.objects.all().order_by('waktu_mulai')

    paginator = Paginator(diklat,5)
    page = request.GET.get('page')
    try:
        diklat = paginator.page(page)
    except PageNotAnInteger:
        diklat = paginator.page(1)
    except EmptyPage:
        diklat = paginator.page(paginator.num_pages)
    return render(request, 'tata_usaha/diklat.html', {"diklat":diklat})

"""
Jadwal Dinas Satpam
"""

@login_required(login_url=settings.LOGIN_URL)
def JadwalDinasSatpamView(request):
    jadwalsatpam = None
    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        jadwalsatpam = JadwalDinasSatpam.objects.filter(tanggal__year=tahun, tanggal__month=bulan)
    return render(request, 'tata_usaha/jadwal_satpam.html', {"jadwalsatpam": jadwalsatpam})

"""
Listrik
"""
@login_required(login_url=settings.LOGIN_URL)
def ListrikView(request):
    listrik = ListrikMati.objects.all().order_by('tanggal')


    paginator = Paginator(listrik,5)
    page = request.GET.get('page')
    try:
        listrik = paginator.page(page)
    except PageNotAnInteger:
        listrik = paginator.page(1)
    except EmptyPage:
        listrik = paginator.page(paginator.num_pages)
    return render(request, 'tata_usaha/listrik.html', {"listrik":listrik})

"""
Memo
"""
@login_required(login_url=settings.LOGIN_URL)
def MemoView(request):
    memo = None
    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        memo = Memo.objects.filter(tanggal__year=tahun, tanggal__month=bulan)

    return render(request, 'tata_usaha/memo.html', {"memo":memo})

"""
PEDAWAI
"""
@login_required(login_url=settings.LOGIN_URL)
def PegawaiView(request):
    options = Pegawai.objects.all()

    paginator = Paginator(options,5)
    page = request.GET.get('page')
    try:
        options = paginator.page(page)
    except PageNotAnInteger:
        options = paginator.page(1)
    except EmptyPage:
        options = paginator.page(paginator.num_pages)
    return render(request, 'tata_usaha/pegawai.html', {"options": options})

"""
SURAT KELUAR
"""
@login_required(login_url=settings.LOGIN_URL)
def SuratKeluarView(request):
    keluars = None
    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        keluars = SuratKeluar.objects.filter(tanggal__year=tahun,tanggal__month=bulan)
    return render(request, 'tata_usaha/surat_keluar.html', {"keluars":keluars})

"""
SURAT MASUK
"""
@login_required(login_url=settings.LOGIN_URL)
def SuratMasukView(request):
    masuks = None
    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        masuks = SuratMasuk.objects.filter(tanggal__year=tahun,tanggal__month=bulan)
    return render(request, 'tata_usaha/surat_masuk.html', {"masuks":masuks})