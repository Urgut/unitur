from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tur, Bron
from .forms import BronForm


def home(request):
    return render(request, 'index.html')

@login_required
def tur_royxati(request):
    turlar = Tur.objects.all()
    return render(request, 'tur_royxati.html', {'turlar': turlar})

@login_required
def tur_bronlash(request, tur_id):
    tur = get_object_or_404(Tur, id=tur_id)
    if request.method == 'POST':
        form = BronForm(request.POST)
        if form.is_valid():
            bron = form.save(commit=False)
            bron.foydalanuvchi = request.user
            bron.tur = tur
            bron.save()
            return redirect('bron_qilingan_turlar')
    else:
        form = BronForm()

    return render(request, 'tur_bronlash.html', {'form': form, 'tur': tur})

@login_required
def bron_qilingan_turlar(request):
    bronlar = Bron.objects.filter(foydalanuvchi=request.user)
    return render(request, 'bron_qilingan_turlar.html', {'bronlar': bronlar})
