from django import forms
from django.forms import ModelForm
from tata_usaha.models import *

class AtkForm(forms.ModelForm):

    class Meta:
        model = AlatTulisKantor
        fields = ['tanggal','nama_barang','jumlah','keterangan','petugas','petugas_entri']
