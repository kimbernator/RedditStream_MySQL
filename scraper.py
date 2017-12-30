import db
import sys
import threading
from threading import Thread
import submissionstream
import commentstream

try:
    import bot
except ImportError:
    print("bot.py is missing")
    exit

try:
    import praw
except ImportError:
    print("Praw is missing")
    exit

subreddit = sys.argv[1]
reddit = bot.login()
db.init(subreddit)


def submissions():
    submissionstream.stream_submissions(subreddit, reddit)

def comments():
    commentstream.stream_comments(subreddit, reddit)

if __name__ == '__main__':
    Thread(target = submissions).start()
    Thread(target = comments).start()
