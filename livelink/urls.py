from django.conf.urls import patterns, include, url
from django.contrib import admin
from links.views import Login, Registration, NewLink, Link, logout
from links.views import add_fav, rm_fav

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'livelink.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^link/$', NewLink.as_view(), name='links'),
    url(r'^links/$', Link.as_view(), name='links'),

    url(r'^fav/(?P<id>\d{1,})/$', add_fav, name='fav'),
    url(r'^rfav/(?P<id>\d{1,})/$', rm_fav, name='rfav'),

    url(r'^login/$', Login.as_view()),
    url(r'^logout/$', logout),
    url(r'^signup/$', Registration.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
