from django.contrib import admin
from django.urls import path
from tur import views  # views modulini unitur papkasidan import qilish
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    # Statik fayllar uchun yo'l
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Media fayllar uchun yo'l (agar kerak bo'lsa)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
