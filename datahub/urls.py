from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datahub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('json_bridge.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
