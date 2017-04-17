#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from .models import Entry


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/feed/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Entry.objects.published()[:5]
