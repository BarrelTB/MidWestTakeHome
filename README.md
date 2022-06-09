# MidWestTakeHome

## Installation

Clone repo locally

Run MySQL script (dbScript.sql) to create database and populate with Lorem Ipsum content
OR
Make migrations and migrate, copy/run insert statements from MySQL script (dbScript.sql)

set db connection as such and ensure settings.py reflects:

 'default': {
        'ENGINE'  : 'django.db.backends.mysql', # <-- UPDATED line 
        'NAME'    : 'MidWestTakeHomeDB',        # <-- UPDATED line 
        'USER'    : 'test',                     # <-- UPDATED line
        'PASSWORD': 'Secret_1234',              # <-- UPDATED line
        'HOST'    : 'localhost',                # <-- UPDATED line
        'PORT'    : '3306',

## Notes
Added default python/django .gitignore. 
If anything within is needed contact so I can remove it from the .gitignore.

## Project/App heirarchy
takehome -> base/start
home -> front/views
api -> api
static/static_cdn -> static css files, images, etc.

