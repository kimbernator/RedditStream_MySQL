import db
import time

def stream_comments(subreddit, reddit):
    for comment in reddit.subreddit(subreddit).stream.comments():
        if comment.author is None:
            author = '[DELETED]'
        else:
            author = comment.author.name

        data_form = {
        'idstr': comment.fullname,
        'created': comment.created_utc,
        'author': author,
        'parent': comment.parent_id,
        'submission': comment.link_id,
        'body': comment.body,
        'score': comment.score,
        'subreddit': comment.subreddit.display_name.replace('\'', '').lower(),
        'distinguish': comment.distinguished,
        'link': comment.permalink,
        'textlen': len(comment.body)
        }

        db.insert_comment(data_form)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ": Comment by " + author)
