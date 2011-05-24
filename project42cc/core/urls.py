from django.conf.urls.defaults import *

from core.views import index, add_person


urlpatterns = patterns('',
    (r'^$', index),
    (r'^add_person/$', add_person),
    (r'^login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'login.html'}),
)
