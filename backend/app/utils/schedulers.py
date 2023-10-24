from celery.schedules import crontab

schedule = [
    {
        "name": "update_tweet_count",
        "desc": {
            "task": "app.tasks.tweet.tweet_count",
            "schedule": crontab(minute="*/1"),
        },
    },
    {
        "name": "truncate_table_tweets",
        "desc": {
            "task": "app.tasks.tweet.delete_all_tweets",
            "schedule": crontab(minute=0, hour=0),
        },
    },
]
