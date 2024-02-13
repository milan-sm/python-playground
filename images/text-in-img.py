from PIL import Image, ImageDraw, ImageFont

#img = Image.new(mode, size, color)
#img.save(filename)

img = Image.new('RGB', (500, 500), color = 'red')

fnt = ImageFont.truetype('c:\\Windows\\Fonts\\DejaVuSans.ttf', 230)

d = ImageDraw.Draw(img)
d.text((20, 20), "Ovo je tekst koji treba da se ubaci", fill=('white'))

img.save('testjpg.jpg')
