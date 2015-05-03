from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import SendSMS
from .forms import SendSMSForm
from django.core.urlresolvers import reverse_lazy
from .utils import * 
from datetime import datetime
now = datetime.now()

class SendSmsCreateView(CreateView):
# class SendSmsCreateView():
    model = SendSMS
    form_class = SendSMSForm
    template_name = 'communication/sendsms_form.html'
    success_url = reverse_lazy('send_sms')
    # success_url = reverse('send_sms')    
 
    # def form_valid(self, form):
    def form_valid(self, form):    	
        # number = self.cleaned_data['to_number']
        # body = self.cleaned_data['body']

        number = form.cleaned_data['to_number']
        body = form.cleaned_data['body']        

        # if form.is_valid(): 
        #     number = self.cleaned_data['to_number']
        #     body = self.cleaned_data['body']                
        # call twilio
        sent = send_twilio_message(number, body)
 
        # save form
        send_sms = form.save(commit=False)
        send_sms.from_number = settings.TWILIO_PHONE_NUMBER
        send_sms.sms_sid = sent.sid
        send_sms.account_sid = sent.account_sid
        send_sms.status = sent.status
        # send_sms.sent_at = now()
        if sent.price:
            send_sms.price = Decimal(force_text(sent.price))
            send_sms.price_unit = sent.price_unit
        send_sms.save()
 
        return super(SendSmsCreateView, self).form_valid(form)