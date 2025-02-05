from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tur, Bron
from .forms import BronForm
from django.utils.translation import activate
from django.conf import settings
from django.utils.translation import get_language


def home(request):
    return render(request, 'index.html')

# def set_language(request):
#     lang = request.POST.get('language')
#     activate(lang)
#     response = redirect('home')  # Bu yerda foydalanuvchini 'home' sahifasiga qayta yo'naltiryapsiz
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
#     return response

def set_language(request):
    lang = request.POST.get('language')
    activate(lang)
    print(get_language())  # Hozirgi tilni konsolda ko'rish uchun
    response = redirect('home')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


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
