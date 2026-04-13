from django import forms
from .models import ChaiVarity

class ChaiVarityForm(forms.ModelForm):
    chai_varity = forms.ModelChoiceField(
        queryset=ChaiVarity.objects.all(),
        label="Select Chai Variety"
    )

    class Meta:
        model = ChaiVarity  
        fields = ['chai_varity']