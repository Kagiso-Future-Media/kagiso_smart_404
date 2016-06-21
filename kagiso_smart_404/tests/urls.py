from django.conf import settings
from django.conf.urls import include, patterns, url
from django.shortcuts import render
from wagtail.wagtailcore import urls as wagtail_urls


urlpatterns = patterns(
    '',
    url(r'', include(wagtail_urls)),  
)

handler404 = 'kagiso_smart_404.views.not_found'
