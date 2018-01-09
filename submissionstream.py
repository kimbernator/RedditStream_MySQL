import db
import time

def stream_submissions(subreddit, reddit):
    subdb = db.RDB()
    subdb.start('submissions', subreddit)
    for submission in reddit.subreddit(subreddit).stream.submissions():
        if submission.author is None:
            author = '[DELETED]'
        else:
            author = submission.author.name

        # if not existing_entry:
            if submission.is_self:
                # Selfpost's URL leads back to itself, so just ignore it.
                url = None
            else:
                url = submission.url

        data_form = {
            'idstr': submission.fullname,
            'created': submission.created_utc,
            'self': submission.is_self,
            'nsfw': submission.over_18,
            'author': author,
            'title': submission.title,
            'url': url,
            'selftext': submission.selftext,
            'score': submission.score,
            'subreddit': submission.subreddit.display_name.replace('\'', '').lower(),
            'distinguish': submission.distinguished,
            'link': submission.permalink,
            'textlen': len(submission.selftext),
            'num_comments': submission.num_comments,
            'flair_text': submission.link_flair_text,
            'flair_css_class': submission.link_flair_css_class,
            'augmented_at': None,
            'augmented_count': None,
        }

        subdb.submission(data_form)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ": Submission by " + author)
