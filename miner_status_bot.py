#	miner tweet bot
#	Austin Rawlings
#	23 June 2017

#	Credit to Digital Ocean for having well written tutorials.

#	Define the miner's json url in page.py as: 
#		page = 
#	Define your Twitter account's credentials in creds.py as:
#		consumer_key = 
#		consumer_secret = 
#		access_token = 
#		access_token_secret =

import requests, json, tweepy
from time import sleep

#import twitter creds.py
from creds import *

#import url from page.py
from page import *

#access and authorize twitter creds from creds.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#infinite loop to trigger it once an hour
check = 1
while check == 1:

#read the miners json url
	r = requests.get(page)
	data = json.loads(r.content)
	
#read and define the numbers I care about from the json array
	actual_rate = data["hashRate"]
	reported_rate = data["reportedHashRate"]
	average_rate = data["avgHashrate"]
	average_rate = str(average_rate)
	#I am sure there was an easier way to move the point in the avgHashrate value, it comes in as a float with the point being after 8 digits.
	#I converted it to a string and then pulled the first three characters to use as my new 00.0 output.

#print them to the terminal to check output
	print("Hashing at " + actual_rate + " with an average of " + average_rate[0:2] + "." + average_rate[2] + " MH/s and reported at " + reported_rate + ".")

#tweet the numbers and catch duplicate status error
	try:
		api.update_status("Hashing at " + actual_rate + " with an average of " + average_rate[0:2] + "." + average_rate[2] + " MH/s and reported at " + reported_rate + ".")
	except tweepy.TweepError as error:
		print(error.reason)

#wait an hour before looping
	sleep(3600)
