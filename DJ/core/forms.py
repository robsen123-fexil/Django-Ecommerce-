from django import forms
from django_countries.fields import CountryField
class checkoutforms(forms.Form):
    street_add=forms.CharField()
    apartment_add=forms.CharField(required=False)
    country=CountryField(blank_label='(select country)')
    same_billing_add=forms.BooleanField(widget=forms.CheckboxInput())
    save_info=forms.BooleanField(widget=forms.CheckboxInput())
    payment_method=forms.BooleanField(widget=forms.RadioSelect())