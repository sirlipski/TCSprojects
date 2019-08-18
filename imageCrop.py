from PIL import Image

image_path = 'quoteTesting.png'
image = Image.open(image_path)
w, h = image.size
image.crop((w/2-500, h/2-500, w/2+500, h/2+500)).save('cropped.png')