from django.db import models
from django.contrib.auth.models import User

class Tur(models.Model):
    nom = models.CharField(max_length=100)
    manzil = models.CharField(max_length=200)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    boshlanish_sana = models.DateField()
    tugash_sana = models.DateField()
    tasvir = models.ImageField(upload_to='tur_tasvirlari/', blank=True)

    def __str__(self):
        return self.nom

class Bron(models.Model):
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE)
    tur = models.ForeignKey(Tur, on_delete=models.CASCADE)
    bron_sanasi = models.DateTimeField(auto_now_add=True)
    yolovchilar_soni = models.PositiveIntegerField()
    umumiy_narx = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Umumiy narxni avtomatik hisoblash
        self.umumiy_narx = self.tur.narx * self.yolovchilar_soni
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.foydalanuvchi.username} uchun {self.tur.nom} turi bron qilindi"
