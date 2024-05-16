# app/forms.py
from django import forms

class PotatoForm(forms.Form):
    potato_name = forms.CharField(label='Potato Name', max_length=100)
    potato_description = forms.CharField(label='Potato Description', widget=forms.Textarea)
    potato_number = forms.IntegerField(label='Potato Number')
    is_potato = forms.BooleanField(label='Is Potato', required=False)
