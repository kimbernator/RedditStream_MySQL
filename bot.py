'''
This file will be imported by all bots, and provides a standard way to log in.

You should never place this file in a git repository or any place where it will
get shared.

The requirements for this file are:

1   A function `anonymous` with no arguments, which returns a `praw.Reddit`
    instance that has a Useragent but is otherwise anonymous / unauthenticated.
    This will be used in bots that need to make requests but don't need any
    permissions.

2   A function `login` with optional parameter `r`, which returns an
    authenticated Reddit instance.
    If `r` is provided, authenticate it.
    If not, create one using `anonymous` and authenticate that.
    Either way, return the instance when finished.

The exact workings of these functions, and the existence of any other variables
and functions are up to you.


I suggest placing this file in a private directory and adding that directory to
your `PYTHONPATH` environment variable. This makes it importable from anywhere.

However, you may place it in your default Python library. An easy way to find
this is by importing a standard library module and checking its location:
>>> import os
>>> os
<module 'os' from 'C:\\Python36\\lib\\os.py'>

But placing the file in the standard library means you will have to copy it over
when you upgrade Python.

If you need multiple separate bots, I would suggest creating copies of this file
with different names, and then using `import specialbot as bot` within the
application, so that the rest of the interface can stay the same.
'''

import praw

USERAGENT = ''
APP_ID = ''
APP_SECRET = ''
APP_URI = 'https://127.0.0.1:65010/authorize_callback'
APP_REFRESH = ''
APP_SCOPES = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
APP_ACCOUNT_CODE = ''
# https://www.reddit.com/comments/3cm1p8/how_to_make_your_bot_use_oauth2/

def anonymous():
    r = praw.Reddit(
        user_agent=USERAGENT,
        client_id=APP_ID,
        client_secret=APP_SECRET,
    )
    return r

def login(r=None):
    r = praw.Reddit(
        user_agent=USERAGENT,
        client_id=APP_ID,
        client_secret=APP_SECRET,
        refresh_token=APP_REFRESH,
    )
    return r