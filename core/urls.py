from django.conf.urls import url



urlpatterns = [

    url(r'^$', 'core.views.index', name='index')
]