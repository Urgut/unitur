from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tur', views.tur_royxati, name='tur_royxati'),
    path('set-language/', views.set_language, name='set_language'),
    path('bronlash/<int:tur_id>/', views.tur_bronlash, name='tur_bronlash'),
    path('bron-qilingan-turlar/', views.bron_qilingan_turlar, name='bron_qilingan_turlar'),
    
]
