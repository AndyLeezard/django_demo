from django import forms
from datetime import date, timedelta

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email address')
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'min': date.today() + timedelta(days=1)}))