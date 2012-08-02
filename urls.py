from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gezipuzi.views.home', name='home'),
    # url(r'^gezipuzi/', include('gezipuzi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^puzi/(?P<id>\d+)/like$', 'like.views.plus'),
    # Uncomment the next line to enable the admin:
     url(r'^puzi/(?P<id>\d+)/$', 'puzi.views.show'),
   
     url(r'^admin/', include(admin.site.urls)),
)
