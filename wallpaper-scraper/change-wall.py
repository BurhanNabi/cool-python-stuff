#!/usr/bin/env python
# -*- coding: utf-8 -*-

import praw
import urllib.request
import os
import pprint

# SUB='earthporn'
SUB='wallpapers'
LIMIT=10

reddit = praw.Reddit( client_id='7cTWvScixi3ZYw',
        client_secret='XiDJMkb6I6hWDnIDoNVe2HlNHGo',
        username='firminosleftpeg',
        password='kuchbhirakhle',
        user_agent='wallpaper getter script' )

print( reddit.user.me() )

submissions = reddit.subreddit(SUB).hot(limit=LIMIT)
url=""
title=""
temp_title=""
ext=""

for s in submissions:
    # FOR SEEING ALL FIELDS
    # pprint.pprint( vars( s ) )
    # exit(0)

    if not s.is_reddit_media_domain: continue
    if s.pinned: continue

    # Get name and image
    title = s.title
    url = s.url
    ext = url.split('.')[-1]
    title = title +"."+ ext
    title = title.replace( " ","")
    temp_title="top"+"."+ext
    urllib.request.urlretrieve( url, temp_title )
    break

# Copy to wallpapers
final_dest = '/home/bnabi/Pictures/reddit-wallpapers/' + title
command = 'cp ' + temp_title + ' ' + final_dest 
os.system( command )

# Set as background
location_arg = '"file://' + final_dest +'"'
print( location_arg )
command = 'gsettings set org.gnome.desktop.background picture-uri ' + location_arg
os.system( command )

# Notify the user
os.system( "notify-send 'Wallpaper Changed!' 'Cool automatic script has changed wallpaper!' --icon=dialog-information" )

