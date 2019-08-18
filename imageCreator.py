from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
from datetime import datetime

def getAquote():
    lines = open('movie_quotes_final.txt').read().split("\n\n")
    myline = lines[random.randint(1,len(lines))]
    return myline.strip()
    with open('movie_quotes_final.txt', "w") as f:
        for line in lines:
            if line.strip('\n\n') != myline:
                f.write(line)


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


imageCreate(text,color,font,fontSize,'quoteTesting2.png')