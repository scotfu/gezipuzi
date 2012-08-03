from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
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

#if settings.DEBUG:
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, },
        name='media'),
        )
urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, },
        name='static'),
        )
