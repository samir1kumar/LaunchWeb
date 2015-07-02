from django.conf.urls import url



urlpatterns = [

    url(r'^$', 'core.views.index', name='index'),
    url(r'^(?P<ref_id>.*)$', 'core.views.share', name='share'),
]