from django import forms

class checkforms(forms.form):
    street_add=forms.CharField()
    apartment_add=forms.Charfield(required=False)
    