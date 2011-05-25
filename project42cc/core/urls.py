from django.conf.urls.defaults import *

from core.views import index, edit_person, requests


urlpatterns = patterns('',
    (r'^$', index),
    (r'^requests/$', requests),
    (r'^edit_person/$', edit_person),
    (r'^login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'login.html'}),
)
