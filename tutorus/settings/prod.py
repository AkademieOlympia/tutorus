import dj_database_url

from base import *

DATABASES = {'default': dj_database_url.config(default='postgres://cynxhwmdptcgih:1Rhc-q2Wy7kpnDuvbJQNn8j6gY@ec2-107-20-224-107.compute-1.amazonaws.com/d6cjeo6acbuta9')}

STATIC_URL = "http://s3.amazonaws.com/tutorus/"