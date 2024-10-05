from PIL import Image, ImageDraw, ImageFont

import sys

image_path = "test.jpg"
origin = Image.open(image_path)

origin = origin.convert("RGB")
r, g, b = origin.split()
dominant_color = {"Red": 0, "Green": 0, "Blue": 0}
for pixel in origin.getdata():
    dominant_color["Red"] += pixel[0]
    dominant_color["Green"] += pixel[1]
    dominant_color["Blue"] += pixel[2]
max_value = max(dominant_color.values())
for color in dominant_color:
    if dominant_color[color] == max_value:  #
        print(color)