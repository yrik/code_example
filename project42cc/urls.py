from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('core.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    )
urlpatterns += staticfiles_urlpatterns()
