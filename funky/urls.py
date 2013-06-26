from django.conf.urls import patterns, include, url
from chuli.views import Puli

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'funky.views.home', name='home'),
    # url(r'^funky/', include('funky.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'chuli.views.index'),
    url(r'^search/$', 'chuli.views.search')
    #url(r'^search/(?P<q>[.*])/', 'chuli.views.search'),
)
