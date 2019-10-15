import os
import praw
import time

from settings import(app_key,app_secret,subreddit_name)


reddit_client = praw.Reddit(client_id = app_key,
			    client_secret = app_secret,
			    user_agent = ('android:'
					'com.ayam.subredditnotif:v0.1'
					'(by /u/AyamDobhal)')
				)

subreddit = reddit_client.subreddit(subreddit_name)
print("established connection with the subreddit!")

def post_fetcher(SUBREDDIT):
	new_submissions = []
	for submission in subreddit.new(limit=20):
		new_submissions.append(submission.id)
	return new_submissions
while True:
	print("Fetching submissions.")
	submissions_1 = post_fetcher(subreddit)
	time.sleep(60)
	submissions_2 = post_fetcher(subreddit)
	if submissions_1 == submissions_2:
		print("No new submissions so far. Is your favorite subreddit dead?")
		continue
	else:
		print("Found new submissions! Sending notification.")
		os.system('''termux-notification -t "{} has new submissions"'''.format(subreddit_name))
		continue
