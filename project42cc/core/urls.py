from django.conf.urls.defaults import *

from core.views import index


urlpatterns = patterns('',
    (r'^$', index),

)
