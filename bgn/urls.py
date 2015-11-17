"""bgn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bgn_app.views import *

urlpatterns = [
    url(r'^around_me/', around_me, name="around_me"),
    url(r'^events/$', get_users_events, name="events"),
    url(r'^guilds/', get_users_guilds, name="guilds"),
    url(r'^users/', users, name="users"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^games/', games, name="games"),
    url(r'^events/create/$', event_create, name="event_create"),
    url(r'^guild_detail/(\d+)/$', guild_detail, name="guild_detail"),
    url(r'^event_detail/(\d+)/$', event_detail, name="event_detail"),
    # url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()