from InstagramAPI import InstagramAPI
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os
import sys
import shutil
from imageCreator import imageCreate, getAquote
from datetime import datetime, timedelta
import random
import time as t

username = 'tonyanevko'
password = 'asdfghjkl123'
image = '/Users/ivan.lipski/Desktop/newWork/pics/pic2.jpg'
text = "Hello, Friend.\n\n\n.\n\n\nI'm Tonya Nevko, an experimental machine built\nto make your day a bit better\nby showing an inspiring quote.\n\n\n.\n\n\nAs long as my Creator's will remains,\nI will become more and more \ncomplex algorithm."
caption = '#bot #coding #2019 #everydayimprove #testing'


#globalImageNumber
InstagramAPI = InstagramAPI(username, password)


def get_image(url):
    f = open('pic1.jpg','wb')
    f.write(requests.get(url).content)
    f.close() 
    shutil.move('/Users/ivan.lipski/Desktop/newWork/pic1.jpg', '/Users/ivan.lipski/Desktop/newWork/pics/pic1.jpg')

def upload_photo(image, text):
    photo_path = image
    caption = text
    InstagramAPI.uploadPhoto(photo_path, caption=caption)

#imageForTest = get_image('https://cdn.vox-cdn.com/thumbor/s6cI4NEU9hgaUFjXfyVPMmMc044=/cdn.vox-cdn.com/uploads/chorus_asset/file/3847870/11376655_479893395513491_201556343_n.0.jpg')


while 1:
    InstagramAPI.login()  # login

    text = getAquote()
    red = random.randint(90,255)
    green = random.randint(100,255)
    blue = random.randint(100,255)

    color = (red,green,blue)
    font = '/Library/Fonts/Baskerville.ttc'
    fontSize = 72
    if(red*green*blue > 1000000):
        textColor = 'black'
    else:
        textColor = 'white'

    imageCreate(text,color,font,fontSize,'TonyaTestingAlpha.jpg')
    imageForTest = ('TonyaTestingAlpha.jpg')

    upload_photo(imageForTest,caption)

    dt = datetime.now() + timedelta(hours=12)

    print(datetime.now())

    while datetime.now() < dt:
        t.sleep(100)