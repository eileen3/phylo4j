from django.conf.urls import patterns, include, url

from phylo4j.api.views import api_root, ProteinDetail

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    #website
    (r'^$', 'phylo4j.website.views.index'),

    #api urls
    url(r'^api/$', api_root),
    url(r'^api/protein/(?P<accession>[\w\-]+)/$', ProteinDetail.as_view(), name='protein-detail')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
