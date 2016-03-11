from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # url(r'^$', 'upload.views.home', name='home'),
    url(r'^$', 'ui.views.upload', {'template': 'ui/index.html'}, name='upload'),
)
