import tweepy
from tweepy.api import API
from tweepy import OAuthHandler
# import numpy as np
#from tweepy import Stream
#from tweepy.streaming import StreamListener

import time # standard lib
import csv
import json

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = '5mWncEQOyReUmJruc7HmcvXQP'
CONSUMER_SECRET = 'PV5TjR12TaWmRwdj7RLK4Pew2Y5Lf6i31ZydD2NygMayYHLHt3'
ACCESS_KEY = '2320137758-p24IfFNZpoua5k3DlsAcHhdHn1x3ci6CbeaWQHO'
ACCESS_SECRET = 'LxKSAA9hh34BuU1eCdJa3kqPRUYhY0MgGgXtjdGCprF8S'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
key = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
key.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
alltweets = []	 ## this is the latest starting tweet id
u = api.get_user(962197608)
print 'Username: '+u.screen_name

new_tweets = api.user_timeline(screen_name = "elmo",count=200)
alltweets.extend(new_tweets)
oldest = alltweets[-1].id - 1
while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = "elmo",count=200, include_rts = False, max_id=oldest)
		#save most recent tweets
		alltweets.extend(new_tweets)
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		print "...%s tweets downloaded so far" % (len(alltweets))

print "+++++++++++++++++++"

oldtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
outtweets = [tweet.text.encode("utf-8") for tweet in alltweets]
print outtweets[0:20]
print "+++++++++++++++++++"
elmo_tweets = open('elmo_tweets.txt', 'w')
for tweet in outtweets:
  elmo_tweets.write("%s\n" % tweet)
'''np.savetxt('elmo_tweets.txt', outtweets, fmt='%.18e', delimiter=', ', newline='\n', header='', footer='', comments='# ')
with open('elmo_tweets.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(["id","created_at","text"])
	writer.writerows(oldtweets)
pass'''
