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
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#コマンドライン引数で『user_id』を渡すようにする。
user_id = sys.argv

# 取得数
params ={'user_id' : user_id, 'count' : 5}
res = twitter.get(url, params = params)

timelines = json.loads(res.text)

if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines: #タイムラインリストをループ処理
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)
