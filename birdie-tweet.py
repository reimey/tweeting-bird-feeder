#!/usr/bin/env python

#######################################################################
#
#   Birdie Tweet
#
#   Takes a picture of a bird when it is at the bird feeder 
#   and tweets it to Twitter.
#
#   This program requires python2, twython, and Adafruit_VCNL4000
# 
#   Author:  Mark Reimer
#   Date: August 3, 2014
#######################################################################

from twython import Twython
from subprocess import call
import time
import random
import RPi.GPIO as GPIO


# Initialize GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)   # GPIO4 is pin 7

# Twitter Token
APP_KEY = '<insert_app_key>'
APP_SECRET = '<insert_app_secret>'
ACCESS_TOKEN = '<insert_access_token>'
ACCESS_TOKEN_SECRET = '<insert_access_token_secret>'

SLEEP_DURATION = 30

messages = []
messages.append("The early bird gets the fresh seeds. #birds #birdwatching")
messages.append("This bird just took a selfie. #birds #birdwatching")
messages.append("Thanks for visiting the tweeting bird feeder. #birds #birdwatching")
messages.append("Another happy bird served. #bird #birds #birdwatching")
messages.append("Who ruffled her feathers? #bird #birds #birdwatching")
messages.append("Show me your birdie. #birds #birdwatching #bird")
messages.append("A #bird on the feeder is worth two tweets. #bird #birds #birdwatching")
messages.append("Free as a bird. #birdwatching #birds #bird")
messages.append("Intelligence without ambition is a bird without wings. -Salvador Dali #birdwatching")
messages.append("A bird sitting on a tree is never afraid of the branch breaking, because her trust is not on the branch but on its own wings. -nknown")
messages.append("I think we consider too much the good luck of the early bird and not enough the bad luck of the early worm. -FDR #birdwatching")
messages.append("Hold fast to dreams, for if dreams die, life is a broken-winged bird that cannot fly. -Langston Hughes #birds #birdwatching")
messages.append("Faith is the bird that feels the light when the dawn is still dark. -Rabindranath Tagore #birdwatching #birds")
messages.append("A fish may love a bird, but where would they live? -Drew Barrymore #birds #birdwatching")
messages.append("If you cannot catch a bird of paradise, better take a wet hen. -Nikita Khrushchev #bird #birdwatching")
messages.append("Some newspaper articles are fit only to line the bottom of bird cages. #birdwatching #birds #bird")
messages.append("Some birds aren't meant to be caged. Their feathers are just too bright. -Stephen King #birdwatching #birds")
messages.append("You're so vain, you probably think this selfie is about you. #birdwatching #birds")
messages.append("In order to see birds it is necessary to become a part of the silence. -Robert Lynd #birdwatching #birds")
messages.append("He imagines a necessary joy in things that must fly to eat. -Wendell Berry #birds #birdwatching #bird")



# wait for proximity sensor 
while True:
	if (GPIO.input(04)):
		try:
			# Take a picture
			call("/opt/vc/bin/raspistill -e jpg --vflip -w 320 -h 320 -q 100 -o /tmp/snapshot.jpg", shell=True)

			# Sign in to Twitter
			twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

			# Post a status update with a picture
			photo = open('/tmp/snapshot.jpg', 'rb')
			
			r = random.randint(0, len(messages)-1)
			message = messages[r]
			twitter.update_status_with_media(status=message, media=photo)

		except:
			print("Unexpected error:")
		
		# Sleep so that multiple pictures aren't taken of the same bird
		time.sleep(SLEEP_DURATION)
	
	else:
		time.sleep(0.25)

