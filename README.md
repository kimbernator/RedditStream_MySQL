# RedditStream_MySQL

### Requirements
- Recent Python version. This was developed using 3.6.0.
- PRAW 5 - This was initially made using 5.2, but 5.3 has also been tested and seems to work fine.
- Created an OAuth app at https://reddit.com/prefs/apps. Make it script type, and set the redirect URI to http://localhost:8080. The title and description can be anything you want, and the about URL is not required.
- Use [this PRAW script](https://praw.readthedocs.io/en/latest/tutorials/refresh_token.html) to generate a refresh token. Just save it as a .py file somewhere and run it through your terminal / command line. For simplicity's sake, I just choose `all` for the scopes.
- Fill out bot.py with your OAuth information
- Fill out settings.py with your database connection information (The schema in your database must already exist and write permissions must be granted to the user.)

Credit to /u/GoldenSights for some of the above instructions relating to OAuth

### Usage
- python scraper.py <subreddit_name> e.g ```python scraper.py funny```
