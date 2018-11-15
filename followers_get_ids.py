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
follower_ids_url = 'https://api.twitter.com/1.1/followers/ids.json'

#コマンドライン引数で『user_id』を渡すようにする。
user_id = sys.argv[1]

# 取得件数
count = 5

params = {'user_id': user_id, 'count' : count}

req = twitter.get(follower_ids_url, params = params)

if req.status_code == 200:
    followers_users = json.loads(req.text)
    for tweet in followers_users['ids']:
       print tweet
else:
    print("Failed: %d" % req.status_code)
