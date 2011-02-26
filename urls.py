from django.conf.urls.defaults import *
from django.conf import settings
import os

# enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^receiver', include('receiver.urls')),
    (r'^export/', include('couchexport.urls')),
    url(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'receiver/home/'})
    #(r'^couch/', include('djangocouch.urls')),
    #(r'', include('corehq.apps.hqwebapp.urls')),
    #(r'^couchlog/', include('couchlog.urls')),
    
)


#django-staticfiles static/ url mapper
if settings.DEBUG:
    urlpatterns += patterns('staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )