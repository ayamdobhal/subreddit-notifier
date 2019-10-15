#this is the file used by main.py to get all the secret keys
#The secret keys are (to be) stored as ENVIRONMENT VARIABLES
#A sample is given in envlist-sample

#reddit app

app_key = os.getenv("REDDIT_APP_KEY")
app_secret = os.gerenv("REDDIT_APP_SECRET")
subreddit_name = os.getenv("SUBREDDIT")
