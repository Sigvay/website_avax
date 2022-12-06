from django import forms
from .models import *


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchasedEngines
        fields = ('container', 'number', 'mark', 'model', 'year', 'fuel',
                  'engine_mark', 'engine_number', 'weigh', 'warehouse')

