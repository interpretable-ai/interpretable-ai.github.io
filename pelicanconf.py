#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "clean-blog"


AUTHOR = 'Henry, Eddie and some nerds'
SITENAME = 'Interpretable Artificial Intelligence'
SITEURL = 'http://interpretable-ai.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

HEADER_COLOR = 'black'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
