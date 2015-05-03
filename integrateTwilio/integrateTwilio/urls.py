from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('communication.urls')),
    # Examples:
    # url(r'^$', 'integrateTwilio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# from django.conf.urls import patterns, url
 
# from .views import SendSmsCreateView
 
# urlpatterns = patterns('',
#     url(
#         regex=r'^communication/send/sms/$',
#         view=SendSmsCreateView.as_view(),
#         name='send_sms'
#     ),
# )
