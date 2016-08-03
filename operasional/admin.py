from django.contrib import admin
from operasional.models import *
# Register your models here.

class GempabumiAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'origin_time', 'lintang', 'bujur', 'kedalaman', 'magnitudo', 'remark', 'terasa', 'pga_z', 'pga_ns', 'pga_ew','shakemap', 'observer']
    search_fields = ['tanggal','observer']
    fieldsets = [
        (None, {
            'fields':[
                ('tanggal','origin_time'),
                ('lintang','bujur'),
                ('kedalaman','magnitudo'),
                ('remark','terasa'),
                ('pga_z','pga_ns','pga_ew'),
                ('shakemap','observer'),
            ]
        })
    ]
    list_filter = ()
    list_per_page = 25

admin.site.register(Gempabumi,GempabumiAdmin)

class ListrikUdaraAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'stroke','strong','noise','energy','stroke_peak',
                    'strong_peak','noise_peak','energy_peak','energy_ratio_peak',
                    'signal_peak','observer']
    search_fields = ['tanggal','observer']
    list_per_page = 25
    labels = {
        "apm_stroke": "average",
        "apm_strong": "average",
        "apm_noise": 'average',
        "apm_energy": 'average',
        "time_stroke_peak": "time",
        "time_strong_peak": "time",
        "time_noise_peak": "time",
        "time_energy_peak": "time",
        "time_ratio_peak": "time",
        "time_signal_peak": "time"
    }
    fieldsets = [
        (None, {
            'fields': ['tanggal']
        }),('Total',{
            'fields':[
                ('stroke', 'apm_stroke'),
                ('strong', 'apm_strong'),
                ('noise', 'apm_noise'),
                ('energy', 'apm_energy'),
            ]
        }),('Peak', {
            'fields': [
                ('stroke_peak', 'time_stroke_peak'),
                ('strong_peak', 'time_strong_peak'),
                ('noise_peak', 'time_noise_peak'),
                ('energy_peak', 'time_energy_peak'),
                ('energy_ratio_peak', 'time_ratio_peak'),
                ('signal_peak', 'time_signal_peak'),
            ]
        }),(None, {
            'fields': ['observer']
        })
    ]

    list_filter = ('observer', 'tanggal')

admin.site.register(ListrikUdara, ListrikUdaraAdmin)


class HujanAdmin(admin.ModelAdmin):
    list_display = ['tanggal','jumlah','keterangan','observer']
    search_fields = ['tanggal', 'observer']
    list_filter = ('tanggal', 'observer')
    list_per_page = 25

admin.site.register(Hujan, HujanAdmin)

class MagnetbumiAdmin(admin.ModelAdmin):
    list_display = ['tanggal','komponen','jam00','jam01','jam02','jam03',
                 'jam04','jam05','jam06','jam07','jam08',
                 'jam09','jam10','jam11','jam12','jam13',
                 'jam14','jam15','jam16','jam17','jam18',
                 'jam19','jam20','jam21','jam22','jam23','rata_rata']

    list_filter = ('tanggal','komponen')
    list_per_page = 25
    search_fields = ['tanggal','komponen']
    fieldsets = [
        (None, {
            'fields': [
                ('tanggal','komponen'),
                ('jam00','jam01','jam02'),
                ('jam03','jam04','jam05'),
                ('jam06','jam07','jam08'),
                ('jam09','jam10','jam11'),
                ('jam12','jam13','jam14'),
                ('jam15','jam16','jam17'),
                ('jam18','jam19','jam20'),
                ('jam21','jam22','jam23'),
                ('rata_rata'),
            ]
        })
    ]


admin.site.register(Magnetbumi, MagnetbumiAdmin)


class LaporanAdmin(admin.ModelAdmin):
    list_display = ['nama','batas_waktu','penyusun','status']
    search_fields = ['nama', 'penyusun', 'batas_waktu']
    list_filter = ('batas_waktu','penyusun', 'status')
    list_per_page = 25

admin.site.register(Laporan, LaporanAdmin)
