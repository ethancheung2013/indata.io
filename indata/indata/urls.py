from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'indata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'indata_app.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
