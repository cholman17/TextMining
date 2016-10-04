from __future__ import division
import urllib
import csv
from string import punctuation
import numpy as np
import scipy
import sklearn


tweet1 = open("elmo_tweets.txt").read()
tweet2 = open("oscargrouch_tweets.txt").read()
tweet3 = open("cookiemonster_tweets.txt").read()
tweet1_list = tweet1.split('\n')
tweet2_list = tweet2.split('\n')
tweet3_list = tweet3.split('\n')

Elmo = 'elmo_tweets.txt'
Oscar = 'oscargrouch_tweets.txt'
Cookie = 'cookiemonster_tweets.txt'
sesame = [Elmo, Oscar, Cookie]

tweetz = [tweet1_list, tweet2_list, tweet3_list]

files=['negative.txt','positive.txt']
path='http://www.unc.edu/~ncaren/haphazard/'
for file_name in files:
  urllib.urlretrieve(path+file_name,file_name)

pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]

for tweet in tweet1:
    positive_counter=0
    negative_counter=0

    tweet_processed=tweet.lower()

    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1

    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

print '+++++++++++++++++++++++++++++++'
print 'Number of Positive and Negative Words [ELMO]: '
print len(positive_counts)
print len(negative_counts)
output=zip(tweetz,positive_counts,negative_counts)

for tweet in tweet2:
    positive_counter=0
    negative_counter=0

    tweet_processed=tweet.lower()

    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1

    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

print '+++++++++++++++++++++++++++++++'
print 'Number of Positive and Negative Words [OSCAR]: '
print len(positive_counts)
print len(negative_counts)
output=zip(tweetz,positive_counts,negative_counts)

for tweet in tweet3:
    positive_counter=0
    negative_counter=0

    tweet_processed=tweet.lower()

    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1

    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

print '+++++++++++++++++++++++++++++++'
print 'Number of Positive and Negative Words [COOKIE]: '
print len(positive_counts)
print len(negative_counts)
output=zip(tweetz,positive_counts,negative_counts)

print '++++++++++++++++++++++++++++++++'
print 'SENTIMENT ANALYSIS'

from pattern.en import *
print 'Elmo: '+ str(sentiment(tweet1)) #Elmo: (0.3963483989630115, 0.5356215965705012)
print 'Oscar: '+str(sentiment(tweet2)) #Oscar: (0.16815814393939393, 0.38257575757575757)
print 'Cookie: '+str(sentiment(tweet3)) #Cookie: (0.3104059709413679, 0.5874839248971193)

## COSINE SIMILARITY
import matplotlib.pyplot as plt
import os  # for os.path.basename
from sklearn.manifold import MDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

filenames= ['elmo_tweets.txt', 'oscargrouch_tweets.txt', 'cookiemonster_tweets.txt']
vectorizer = CountVectorizer(input='filenames')
dtm = vectorizer.fit_transform(filenames)
vocab = vectorizer.get_feature_names()

type(dtm)
dtm = dtm.toarray()
vocab = np.array(vocab)

dist = 1 - cosine_similarity(dtm)
print '+++++++++++++++++++++++++++++'
print np.round(dist, 5)
print '++++++++++++++++++++++++++++'
print dist[0, 1] #Elmo and Oscar
print dist[1, 2]
print dist[0, 2] #Elmo and Cookie

mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
poss = mds.fit_transform(dist)  # shape (n_components, n_samples)
xs, ys = poss[:, 0], poss[:, 1]
names = [os.path.basename(fn).replace('_tweets.txt', '') for fn in filenames]
for x, y, name in zip(xs, ys, names):
    color = 'red' if "elmo" in name else 'green'
    plt.scatter(x, y, c=color)
    plt.text(x, y, name)
fig = plt.gcf()
plt.show()
fig.savefig('textsimilarity_sesame.png')
