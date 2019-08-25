from InstagramAPI import InstagramAPI
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os
import sys
import shutil
from datetime import datetime, timedelta
import random
import time as t

username = 'login'
password = 'password'
caption = '#bot #coding #2019 #everydayimprove #testing'


#globalImageNumber
InstagramAPI = InstagramAPI(username, password)


def get_image(url):
    f = open('pic1.jpg','wb')
    f.write(requests.get(url).content)
    f.close() 
    #shutil.move('/Users/ivan.lipski/Desktop/newWork/pic1.jpg', '/Users/ivan.lipski/Desktop/newWork/pics/pic1.jpg')

def upload_photo(image, text):
    photo_path = image
    caption = text
    InstagramAPI.uploadPhoto(photo_path, caption=caption)

def deleteQuote(myline):
    with open("movie_quotes_final.txt", "r") as f:
        lines = f.readlines()
    with open("movie_quotes_final.txt", "w") as f:
        for line in lines:
            if line.strip("\n\n") != myline:
                f.write(line)

def getAquote():
    lines = open('movie_quotes_final.txt').read().split("\n")
    myline = lines[random.randint(1,len(lines))]
    deleteQuote(myline)
    return myline.strip()

def imageCreate(text,color,font,fontSize,name):
    image = Image.new('RGB', (1000, 1000), color = color)

    fnt = ImageFont.truetype(font, fontSize)

    d = ImageDraw.Draw(image)
    text_w, text_h = d.textsize(text, fnt)

    lines = ['']*((int)(text_w/700)+1)

    y_pos = (image.height-text_h*len(lines))/2

    line_spacing = d.textsize('A', fnt)[1] + 6

        
    for i in range(len(lines)):
        if d.textsize(text,fnt)[0] > image.width:
            lastSpace = 30
            while (d.textsize(text[0:lastSpace],fnt)[0] < image.width):
                if text[lastSpace] != ' ':
                    lastSpace-=1
                else:
                    break
            lines[i] = text[0:lastSpace]
            text = text[lastSpace+1:len(text)]
        else:
            lines[len(lines)-1] = text
        if lines[i] != '':
            d.text(((image.width - d.textsize(lines[i],fnt)[0])/2, y_pos), lines[i], font = fnt, fill=(textColor))
            i+=1
            y_pos += line_spacing
    image.save(name)
    return image

#imageForTest = get_image('https://cdn.vox-cdn.com/thumbor/s6cI4NEU9hgaUFjXfyVPMmMc044=/cdn.vox-cdn.com/uploads/chorus_asset/file/3847870/11376655_479893395513491_201556343_n.0.jpg')


while 1:
    InstagramAPI.login()  # login

    text = getAquote()
    red = random.randint(90,255)
    green = random.randint(100,255)
    blue = random.randint(100,255)

    color = (red,green,blue)
    font = '/usr/share/fonts/truetype/msttcorefonts/Courier_New.ttf'
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
