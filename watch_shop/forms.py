from django import forms
from . import models

class WatchShopForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = '__all__'