# subreddit-notifier
A simple python script that utilizes praw and termux API to send a notification whenever there is a new submission in the user specified subreddit. Checks for new submissions every minute. Works with termux.

## Usage
clone the repository:
> `git clone https://github.com/AyamDobhal/subreddit-notifier`


install python(if you haven't already):
> `pkg install python`


upgrade pip:
> `pip install --upgrade pip`


install the requirements:
> `pip install -r requirements.txt`


once the requirements are installed, its time to add the environment variables(the reddit app keys and stuff).

Get them by creating a new app at: https://reddit.com/prefs/apps


for client_api:
> `export REDDIT_APP_KEY=<your-key>`


for client_secret:
> `export REDDIT_APP_SECRET=<your-secret-key>`


now, add the name of the subreddit you want notifications for:
> `export SUBREDDIT=<subreddit-name>`


examples for these ENV VARIABLES are given in envlist-sample


finally, if you make it till here without any errors, run this:
> `python main.py`

and you're all set!
