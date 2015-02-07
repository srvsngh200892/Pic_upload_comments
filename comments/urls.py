from django.conf.urls import patterns, include, url
from core.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'core.views.landing_page', name='landing_page'),
    url(r'^login/$', 'core.views.auth_login', name='user_login'),
    url(r'^logout/$', 'core.views.user_logout', name='user_logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^list/$', 'core.views.list', name='list'),
    url(r'^list/home/image/(?P<pid>[a-zA-Z0-9]+)/$', 'core.views.home', name='home'),
    url(r'^list/shared/images/$', 'core.views.list_community_image', name='list_community_image'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
