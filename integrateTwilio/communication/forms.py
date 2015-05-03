from django import forms
from .models import *

class SendSMSForm(forms.ModelForm):
 
    class Meta:
        model = SendSMS
        fields = ('to_number', 'body')