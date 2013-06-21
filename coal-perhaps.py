#! /usr/bin/env python
# Public domain; MZMcBride; 2012

import random

from twitter.api import Twitter
from twitter.oauth import OAuth, read_token_file

import settings

f = open(settings.initial_path + 'coal-wisdom.txt', 'r')
wisdom = f.read().strip('\n').split('\n')
f.close()

oauth_filename = settings.initial_path + 'coal-oauth'
oauth_token, oauth_token_secret = read_token_file(oauth_filename)

poster = Twitter(auth=OAuth(oauth_token,
                            oauth_token_secret,
                            settings.consumer_key,
                            settings.consumer_secret),
                 secure=True,
                 api_version='1.1',
                 domain='api.twitter.com')

# Twitter blocks duplicate posts, so try up to ten times.
for i in range(10):
    try:
        poster.statuses.update(status=random.choice(wisdom))
        break
    except:  # Unnamed!
        continue
