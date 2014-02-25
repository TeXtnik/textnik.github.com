#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'TeXtnik typesetting'
SITENAME = u'TeXtnik'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# Blogroll
LINKS =  (('TUG', 'http://www.tug.org/'),
          ('LaTeX', 'http://latex-project.org/'),
          ('CervanTeX', 'http://www.cervantex.es/'),
          )


# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

TYPOGRIFY = True

# PAGEs settings
PAGE_DIR = ('pages')
ARTICLE_EXCLUDES = (('pages',))
DEFAULT_CATEGORY = u'Blog'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

STATIC_PATHS = ['data']

