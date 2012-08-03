from django.conf.urls.defaults import patterns, include, url

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

        # url(r'^gezipuzi/', include('gezipuzi.foo.urls')),
        # Uncomment the next line to enable the admin:
        url(r'^puzi/(?P<id>\d+)/$','puzi.views.show'),
        url(r'^item/(?P<id>\d+)/like/$','like.views.plus'),
        url(r'^$','items.views.index'),
        url(r'^pu/$','items.views.pu'),
        url(r'^comment/add/$','comments.views.add'),
        url(r'^accounts/login/$','accounts.views.loginview'),
        url(r'^accounts/logut/$','accounts.views.logout'),
        url(r'^accounts/register/$','accounts.views.register'),

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
