#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog import feed
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^feed/', feed.LatestEntriesFeed(), name='feed'),
    url(r'^$', views.home, name='index'),
    url(r'^blog/(?P<slug>\S+)/$', views.BlogDetail.as_view(), name='entry_detail'),
    url(r'^categories/', views.cat_view,  name='categories'),
    url(r'^tags/', views.tags_view, name='tags'),
    url(r'^about/', views.about_view, name='about'),

    url(r'^tag/(?P<tag_slug>\S+)/$', views.show_by_tag, name='show_by_tag'),
    url(r'^category/(?P<category_slug>\S+)/$', views.show_by_category, name='show_by_category'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.show_by_archive, name='show_by_archive')
]
