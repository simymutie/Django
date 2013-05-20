from django.conf.urls import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()
from django.views.static import * 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os,sys
from django.contrib.auth import views as auth_views

from registration.views import *


urlpatterns = patterns('',
      url(r'^admin/', include(admin.site.urls)),
     url(r'^$','pages.views.MainHomePage'),
     url(r'^home/$','pages.views.MainHomePage'),
     url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', include('contact_form.urls')),
     #urls(r'^search/', include('haystack.urls')),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
          
)
