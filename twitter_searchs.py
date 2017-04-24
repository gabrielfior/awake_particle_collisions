# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:00:52 2016

@author: gabrielfior
"""

#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

#from twitter import *
import twitter
import unicodedata
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import numpy as np


#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
consumer_key="Dm5WXJWNIefzbFRLihnXrs9tW"
consumer_secret="BSVTfcDTKhlVbdmYV8IE3GO9FFmOkYHspW5aH5nMnLkrLMJ5aJ"
access_token="758766990077157376-mKMDLDKDiM0I6AxcJaq5UCLxQ84JB5g"
access_token_secret="6WI7ISGQyATU6xL9xIkTosBu6gWYrNrQkFa0AaVKedfwV"

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter1 = twitter.Twitter(
		        auth = twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret))


#-----------------------------------------------------------------------
# perform a basic search
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
#query = twitter1.search.tweets(q = "temer",lang='pt',count=100)
#query = twitter1.search.tweets(q = "#foratemer",lang='pt',count=100)

"""
def tweets(self, keywords='', follow='', to_screen=True, stream=True,
		   limit=100, date_limit=None, lang='en', repeat=False,
		   gzip_compress=False):


"""
                      


#statuses = api.GetUserTimeline(screen_name=user)
#t.statuses.user_timeline(screen_name="billybob")
#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
print 'num results: ' + str(len(query['statuses']))

#for result in query["statuses"]:
#	print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])

