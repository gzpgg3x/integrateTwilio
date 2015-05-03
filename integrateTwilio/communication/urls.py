from django.conf.urls import patterns, url
 
from .views import SendSmsCreateView
 
urlpatterns = patterns('',
    url(
        regex=r'^communication/send/sms/$',
        view=SendSmsCreateView.as_view(),
        name='send_sms'
    ),
)