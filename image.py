# This file is for finding of images to be displayed!
# Using danbooru's api  https://danbooru.donmai.us/wiki_pages/43568

import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def getImage():
    img = ""

    payload = {
        "tags": config['danbooru']['tags'],
        "limit": 10,
        "random": True,
        "login": config['danbooru']['login'],
        "api_key": config['danbooru']['api_key']
    }

    res = requests.get('https://danbooru.donmai.us/posts.json', params=payload)


    json = res.json()

    output = []
    for i in json:
        # print("score: " + str(i.get('score')))
        # print('source: ' + i.get('source'))

        if i.get('score') > 1 and 'pixiv' in i.get('source'):
            output = [i.get('file_url'),
                      'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + str(i.get('pixiv_id'))]
            break

    if len(output) == 0:
        getImage()
    else:
        return output
