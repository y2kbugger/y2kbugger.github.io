#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'zak kohler'
SITENAME = 'y2kbugger'
SITEURL = ''

PATH = 'content'
THEME = 'themes/william-pelican/'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%Y.%m.%d @ %H:%M:%S'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = [
    ("y2kbugger", '/index.html'),
    ('Tags', '/tags.html'),
    # ('About', '/pages/about.html'),
]
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/favicon.ico',
    'images', 'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

HEAD_EXTRA = u"""
    <link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48 64x64" type="image/vnd.microsoft.icon">
"""

COPYRIGHT = """zak kohler 2017 &mdash; Happy Hacking"""

# ENABLE_SLICKNAV = True
