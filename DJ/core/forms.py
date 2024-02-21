from django import forms
from django_countries.fields import CountryField
payment_option=(('p','paypal'), ('s','stripe'))
class checkoutforms(forms.Form):
    firstname=forms.CharField() 
    email=forms.CharField()
    lastname=forms.CharField()
    street_add=forms.CharField()
    country=CountryField(blank_label='(select country)')
    same_billing_add=forms.BooleanField(widget=forms.CheckboxInput())
    save_info=forms.BooleanField(widget=forms.CheckboxInput())
    payment_method=forms.ChoiceField(widget=forms.RadioSelect(), choices= payment_option)