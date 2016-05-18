#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'libgd.org'
SITENAME = u'GD Graphics Library'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (
          ('Downloads', 'https://github.com/libgd/libgd/releases'),
          ('Issues', 'https://github.com/libgd/libgd/issues'),
#          ('Wiki', 'https://github.com/libgd/libgd/wiki'),
         )

# Social widget
SOCIAL = (#('You can add links in your config file', '#'),
          ('github', 'https://github.com/libgd/libgd'),
         )

PAGE_EXCLUDES = ['manuals']
ARTICLE_EXCLUDES = ['manuals']
STATIC_PATHS = ['manuals']

DEFAULT_PAGINATION = 10

THEME = 'libgd'
