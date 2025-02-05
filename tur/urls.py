from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.tur_royxati, name='tur_royxati'),
    path('bronlash/<int:tur_id>/', views.tur_bronlash, name='tur_bronlash'),
    path('bron-qilingan-turlar/', views.bron_qilingan_turlar, name='bron_qilingan_turlar'),
    
]
