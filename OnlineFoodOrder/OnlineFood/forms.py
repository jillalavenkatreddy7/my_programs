from .models import AddFood,CustomerOrder,AddNewCustomer
from django import forms
class OderForm(forms.ModelForm):
    class Meta:
        model=CustomerOrder
        fields=['Food_type']