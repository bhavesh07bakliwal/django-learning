from django import forms
from .models import ChaiVarity, Store

class ChaiVarityForm(forms.ModelForm):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), label="Select Chai Varity")
    