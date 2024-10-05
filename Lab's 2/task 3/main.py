from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

import sys

image_path = "test.jpg"
origin = Image.open(image_path)

added_image = "img.png"
icon = Image.open(added_image)

icon = icon.resize((30, 30))

draw = ImageDraw.Draw(origin)
font = ImageFont.truetype('arial.ttf', size=20)

width, height = origin.size

draw.text((width - 120, height - 35), "By Yr4as", fill='blue', font=font)
origin.paste(icon, (width - 30, height - 40), icon)

current_directory = os.path.dirname(os.path.abspath(__file__))

save_path = os.path.join(current_directory, "output_image.jpg")

origin.save(save_path)

origin.show()
