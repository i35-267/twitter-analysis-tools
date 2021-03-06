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
user_search_url = 'https://api.twitter.com/1.1/users/search.json'
follower_ids_url = 'https://api.twitter.com/1.1/followers/ids.json'

# Input keywoard
print u'検索したいキーワードを入力してください。'
keyword = raw_input('>> ')

#keyword = sys.argv[1]
keyword_params = {'q': keyword ,'page' : 20 ,'count': 20}

keyword_req = twitter.get(user_search_url, params = keyword_params)

if keyword_req.status_code == 200:
    search_users = json.loads(keyword_req.text)
    for tweet in search_users:
        print '-----------------------------------------------'
        print "キーワード 『" + keyword + "』でユーザーを検索します。|"
        print "以下のユーザーが引っかかりました。|"
        print tweet['name']+ " :: " + tweet['id_str'] + "|"
        print '-----------------------------------------------'

        followers_params = {'user_id': tweet['id_str']}
        followers_req = twitter.get(follower_ids_url, params = followers_params)

        if followers_req.status_code == 200:
            followers_users = json.loads(followers_req.text)
            print "フォロアーを取得していきます。"
            for follers_ids in followers_users['ids']:
                print follers_ids
        else: #正常通信出来なかった場合
            print("Failed: %d" % followers_req.status_code)
else:
    print ("Error: %d" % keyword_req.status_code)
