#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-07-23 18:14
# Last modified: 2017-07-23 18:52
# Filename: settings_dev.py
# Description:
"""
    Author: tianwei
    Email: liutianweidlut@gmail.com
    Description: Django setting for daily development
    Created: 2013-4-12
"""
from settings import *  # 导入 settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'Education_tempdb',             # Or path to database file if using sqlite3.
        #'NAME': 'EducationSystem',
        'NAME': 'EducationSystemBak', # 那次误删之前的数据库备份
        'USER': 'zjs',
        'PASSWORD': 'zjs',
        # 'USER': 'root',                       # Not used with sqlite3.
        # 'PASSWORD': 'root',                   # Not used with sqlite3.
        # 'HOST': '192.168.2.79',                           # Set to empty string for localhost. Not used with sqlite3.
        # 'HOST':'192.168.20.106',
        'PORT': '3306',                           # Set to empty string for default. Not used with sqlite3.
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'EducationSystem',             # Or path to database file if using sqlite3.
#         'USER': 'root',                       # Not used with sqlite3.
#         'PASSWORD': 'root',                   # Not used with sqlite3.
#         'HOST': '192.168.20.106',                           # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '3306',                           # Set to empty string for default. Not used with sqlite3.
#     }
# }

# Website settings
WEB_TITLE = "Province Management Dev"
