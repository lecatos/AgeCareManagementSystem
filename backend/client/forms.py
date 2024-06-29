from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Client
 
        # specify fields to be used
        fields = ["email"]