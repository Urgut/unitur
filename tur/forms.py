from django import forms
from .models import Bron

class BronForm(forms.ModelForm):
    yolovchilar_soni = forms.IntegerField(min_value=1, label="Yo'lovchilar soni")

    class Meta:
        model = Bron
        fields = ['tur', 'yolovchilar_soni']
