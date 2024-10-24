from PIL import Image, ImageDraw, ImageFont

def new_p(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))

def new_p_2(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 10, h // 10))

im = new_p("photo1.jpeg")
im_2 = new_p_2("photo2.png")

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("ofont.ru_Uncage.ttf", 20)
draw.text((15, 260), "Я прошла Афганскую войну", font = font)

im.paste(im_2, (380, 230))
im.show()