from django.conf.urls.defaults import patterns, include, url

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

        # url(r'^gezipuzi/', include('gezipuzi.foo.urls')),
        # Uncomment the next line to enable the admin:
        url(r'^puzi/(?P<id>\d+)/$','puzi.views.show'),
        url(r'^puzi/(?P<id>\d+)/like/$','like.views.plus'),
        url(r'^$','puzi.views.index'),
        url(r'^admin/', include(admin.site.urls)),
)

#if settings.DEBUG:
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, },
        name='media'),

       url(r'^static/admin/(?P<path>.*)$',
        'django.views.static.serve',
       {'document_root': settings.ADMIN_MEDIA_ROOT},
        name='static-admin'),     
         )
urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, },
        name='static'),
        )
