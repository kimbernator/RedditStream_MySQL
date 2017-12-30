import mysql.connector
from settings import db_host, db_user, db_password, db_schema

conn = mysql.connector.Connect(host=db_host,user=db_user,password=db_password,database=db_schema)
cursor = conn.cursor(buffered=True)

DB_INIT_SUBMISSIONS = """
CREATE TABLE IF NOT EXISTS %s_submissions(
    idstr VARCHAR(10),
    created INT,
    self INT,
    nsfw INT,
    author TEXT,
    title TEXT,
    url TEXT,
    selftext TEXT,
    score INT,
    subreddit TEXT,
    distinguish INT,
    link TEXT,
    textlen INT,
    num_comments INT,
    flair_text TEXT,
    flair_css_class TEXT,
    augmented_at INT,
    augmented_count INT
);
"""

DB_INIT_COMMENTS = """
CREATE TABLE IF NOT EXISTS %s_comments(
    idstr VARCHAR(10),
    created INT,
    author TEXT,
    parent TEXT,
    submission TEXT,
    body TEXT,
    score INT,
    subreddit TEXT,
    distinguish TEXT,
    link TEXT,
    textlen INT
);"""

DB_ENTRY_C_1 = "INSERT INTO %s_comments "
DB_ENTRY_C_2 = ("(idstr, created, author, parent, submission, body, score, subreddit, distinguish, link, textlen)"
                "VALUES (%(idstr)s, %(created)s, %(author)s, %(parent)s, %(submission)s, %(body)s, %(score)s, %(subreddit)s, %(distinguish)s, %(link)s, %(textlen)s)")

DB_ENTRY_S_1 = "INSERT INTO %s_submissions "
DB_ENTRY_S_2 = ("(idstr, created, self, nsfw, author, title, url, selftext, score, subreddit, distinguish, link, textlen, num_comments, flair_text, flair_css_class, augmented_at, augmented_count)"
                "VALUES (%(idstr)s, %(created)s, %(self)s, %(nsfw)s, %(author)s, %(title)s, %(url)s, %(selftext)s, %(score)s, %(subreddit)s, %(distinguish)s, %(link)s, %(textlen)s, %(num_comments)s, %(flair_text)s, %(flair_css_class)s, %(augmented_at)s, %(augmented_count)s)")

def init(subreddit):
    cursor.execute(DB_INIT_SUBMISSIONS % subreddit)
    cursor.execute(DB_INIT_COMMENTS % subreddit)
    conn.commit()
    cursor.execute('SET NAMES utf8mb4;')

def insert_comment(data_form):
    cursor.execute(DB_ENTRY_C_1 % data_form['subreddit'] + DB_ENTRY_C_2, data_form)
    commit()

def insert_submission(data_form):
    cursor.execute(DB_ENTRY_S_1 % data_form['subreddit'] + DB_ENTRY_S_2, data_form)
    commit()

def commit():
    conn.commit()

def close():
    cursor.close()
    conn.close()
