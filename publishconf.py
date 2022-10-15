#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

MENUITEMS = [(text, link) for text,link in MENUITEMS if text != 'Drafts']


DEBUG = False
SITEURL = 'http://blog.y2kbugger.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS = "UA-111274102-1"

HEAD_EXTRA_PROD = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0V39RV6EWP"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-0V39RV6EWP');
</script>
"""

HEAD_EXTRA = HEAD_EXTRA_COMMON + HEAD_EXTRA_PROD

SHOW_DRAFTS = False
