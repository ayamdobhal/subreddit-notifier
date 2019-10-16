# subreddit-notifier
A simple python script that utilizes praw and termux API to send a notification whenever there is a new submission in the user specified subreddit. Checks for new submissions every minute. Works with termux.

It uses the reddit api to fetch the 20 latest submissions from the subreddit that the user specifies every 60 seconds and then checks for any new submissions. If there are any new submissions, it sends a notification to the android device using the **termux-notification** command of the [termux-api](https://github.com/termux/termux-api).
