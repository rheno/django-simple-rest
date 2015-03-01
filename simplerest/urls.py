from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest.views import get_response, post_response, put_response, patch_response, delete_response

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplerest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/get', 'rest.views.get_response'),
    url(r'^rest/post', 'rest.views.post_response'),
    url(r'^rest/put', 'rest.views.put_response'),
    url(r'^rest/patch', 'rest.views.patch_response'),
    url(r'^rest/delete', 'rest.views.delete_response'),
)
