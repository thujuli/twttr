from celery import shared_task
from app.core.extensions import db
from app.models import User, Tweet, TweetCount


@shared_task(ignore_result=False)
def tweet_count():
    users = User.query.all()
    user_posts = {}
    for user in users:
        post_count = Tweet.query.filter_by(user_id=user.id).count()
        user_posts[user.username] = post_count

    sorted_users = sorted(user_posts.items(), key=lambda x: x[1], reverse=True)
    existing_trending_users = TweetCount.query.all()
    existing_users = {
        trending_user.username: trending_user
        for trending_user in existing_trending_users
    }

    for username, post_count in sorted_users:
        if username in existing_users:
            # Update entry
            trending_user = existing_users[username]
            trending_user.count = post_count
        else:
            # Create new entry
            trending_user = TweetCount(username=username, count=post_count)
            db.session.add(trending_user)

    db.session.commit()


@shared_task(ignore_result=False)
def delete_all_tweets():
    db.session.query(Tweet).delete()
    db.session.commit()
