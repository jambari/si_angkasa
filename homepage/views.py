from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from tata_usaha.models import *
from operasional.models import *
from django.db.models.functions import Coalesce
from django.utils import timezone
from datetime import datetime, date
# Create your views here.

def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = JenisAkun.objects.get(akun=user.id)
                    login(request, user)

                    request.session['pegawai_id'] = akun.pegawai_id
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']
                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data Pegawai,silahkan hubungi administrator')
                return redirect ('/')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')
    return render (request, 'homepage/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url=settings.LOGIN_URL)
def adminhome(request):
    hari = datetime.today()
    precipitation = Hujan.objects.latest('tanggal')
    earthquake = Gempabumi.objects.latest('tanggal')
    laporan = Laporan.objects.order_by(Coalesce('batas_waktu','penyusun').desc())[:3]
    petir = ListrikUdara.objects.latest('tanggal')
    magnetbumi = Magnetbumi.objects.latest('tanggal')
    memo = Memo.objects.order_by(Coalesce('tanggal','dari').desc())[:3]
    satpam = JadwalDinasSatpam.objects.filter(tanggal__year=hari.year, tanggal__month=hari.month, tanggal__day=hari.day)
    listrik = ListrikMati.objects.latest('tanggal')
    surat_keluar = SuratKeluar.objects.latest('tanggal')
    surat_masuk = SuratMasuk.objects.latest('tanggal')
    user = request.session['username']
    return render(request, 'homepage/adminhome.html', {
        "precipitation": precipitation,
        "earthquake": earthquake,
        "laporan": laporan,
        "petir": petir,
        "magnetbumi": magnetbumi,
        "memo": memo,
        "satpam": satpam,
        "listrik": listrik,
        "surat_keluar": surat_keluar,
        "surat_masuk": surat_masuk,
        "user": user
    })
