from django.conf.urls import url, patterns
from django.conf import settings

from views import index


urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)