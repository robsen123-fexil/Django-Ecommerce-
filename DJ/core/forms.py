from django import forms
from django_countries.fields import CountryField
payment_option=(('p','paypal'), ('s','stripe'))
class checkoutforms(forms.Form):
    street_add=forms.CharField()
    apartment_add=forms.CharField(required=False)
    country=CountryField(blank_label='(select country)')
    same_billing_add=forms.BooleanField(widget=forms.CheckboxInput())
    save_info=forms.BooleanField(widget=forms.CheckboxInput())
    payment_method=forms.ChoiceField(widget=forms.RadioSelect(), choices= payment_option)