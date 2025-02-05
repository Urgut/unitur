from django.contrib import admin
from django.urls import path, include
from tur import views  # views modulini tur papkasidan import qilish
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.home, name='home'),  # Asosiy sahifa
    path('admin/', admin.site.urls),  # Admin panel
    path('i18n/', include('django.conf.urls.i18n')),  # Til o'zgartirish yo'li
]

if settings.DEBUG:
    # Statik fayllar uchun yo'l
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Media fayllar uchun yo'l (agar kerak bo'lsa)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
