from django import forms
from .models import Account


class RForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['fname','lname','email','']