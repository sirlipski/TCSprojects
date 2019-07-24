from PIL import Image, ImageDraw, ImageFont

def imageCreate(text,color,font,fontSize,name):
    image = Image.new('RGB', (1000, 1000), color = color)

    fnt = ImageFont.truetype(font, fontSize)

    d = ImageDraw.Draw(image)
    text_w, text_h = d.textsize(text, fnt)

    y_pos = (image.height-text_h)/2
    x_pos = (image.width-text_w)/2

    d.text((x_pos, y_pos), text, font = fnt, fill=(0,0,0))

    image.save(name)
    return image

#"Hello, Friend.\n\n\n.\n\n\nI'm Tonya Nevko, an experimental machine built\nto make your day a bit better\nby showing an inspiring quote.\n\n\n.\n\n\nAs long as my Creator's will remains,\nI will become more and more \ncomplex algorithm."