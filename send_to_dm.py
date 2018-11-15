# coding: utf-8
import json, config
import sys
import requests
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# URL for keyword search
url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'

recipient_id = sys.argv[1]
params = {"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "recipient_id"}, "message_data": {"text": "Hello World!"}}}}
res = twitter.post(url, params = params)

if res.status_code == 200: #正常通信出来た場合
   dmlist=json.loads(res.text)
   print("成功")
else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)
