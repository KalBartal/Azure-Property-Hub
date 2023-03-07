from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'address',
                  'price', 'bedrooms', 'bathrooms', 'photo']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class PropertySearchForm(forms.Form):
    search = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)
