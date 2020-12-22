#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

DEBUG = False
SITEURL = 'http://blog.y2kbugger.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
UTTERANCES_REPO = 'y2kbugger/y2kbugger.github.io'
UTTERANCES_THEME = 'github-light'
UTTERANCES_LABEL = 'utterances'

GOOGLE_ANALYTICS = "UA-111274102-1"

HEAD_EXTRA = HEAD_EXTRA_PROD

SHOW_DRAFTS = False
