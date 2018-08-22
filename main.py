import time
import schedule

import twitter
import image


def post():
    imgReturn = image.getImage()
    try:
        # print("img: " + imgReturn[1])
        twitter.createTweet(imgReturn[0], imgReturn[1])
    except Exception as e:
        print(e)


print("Bot started")

schedule.every(60).minutes.do(post)

post()
while True:
    schedule.run_pending()
    time.sleep(60)
