# -*- coding: utf-8 -*-
"""
URLs for customerdataapi.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from django.views.static import  serve
from customerdataapi.views import ApiDataViewSet, ApiDataList
from django.conf import  settings
ROUTER = DefaultRouter()
ROUTER.register(r'data', ApiDataViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^api/v1/buscar/(?P<ticker>.+)/$', ApiDataList.as_view()),
    url(r'^api/v1/', include(ROUTER.urls)),
    url(r'^$', TemplateView.as_view(template_name="api/base.html")),

    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT} ) ,


]
