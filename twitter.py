# This file is for updating twitter status!

import io
import requests
from TwitterAPI import TwitterAPI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

maidBotTwitter = ""

api = TwitterAPI(config['twitter']['consumer'],
                 config['twitter']['consumer_secret'],
                 config['twitter']['token'],
                 config['twitter']['token_secret'])


def createTweetStub(imglink, imgSource):
    if imglink and imgSource:
        print('Uploaded: ' + imgSource)


def createTweet(imglink, imgSource):
    res = requests.get(imglink)
    image_file = io.BytesIO(res.content)
    r = api.request('media/upload', None, {'media': image_file})
    if r.status_code == 200:
        media_id = r.json()['media_id']
        r = api.request('statuses/update', {'status': imgSource, 'media_ids': media_id})
        print('Uploaded: ' + imgSource if r.status_code == 200 else 'UPDATE STATUS FAILURE')
