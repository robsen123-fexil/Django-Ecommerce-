from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django.contrib.auth.forms import User
payment_option=(('p','paypal'), ('s','stripe'))
class checkoutforms(forms.Form):
    firstname=forms.CharField(max_length=10) 
    email=forms.CharField(max_length=10)
    lastname=forms.CharField(max_length=10)
    address1=forms.CharField(max_length=20)
    address2=forms.CharField(max_length=20)
    state=forms.CharField(max_length=20)
    country = forms.CharField(max_length=20)
    same_billing_add=forms.BooleanField(widget=forms.CheckboxInput())
    save_info=forms.BooleanField(widget=forms.CheckboxInput())
    payment_option=forms.ChoiceField(widget=forms.RadioSelect(), choices= payment_option)
    ziyp=forms.CharField(max_length=20)
class loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=10)
