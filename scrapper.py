#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='personal_script_14_chars', \
                     client_secret='secret_27_chars_code', \
                     user_agent='your_app_name', \
                     username='redit_username', \
                     password='Reddit_password')

subreddit = reddit.subreddit('subreddit_name') ;

top_subreddit = subreddit.top(limit=200) #Set a limit yourself, max 1000.

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "created": [], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_dict = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_dict["created"].apply(get_date)

topics_data = topics_dict.assign(timestamp = _timestamp)

topics_data.to_csv('file_name.csv')
