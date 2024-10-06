from PIL import Image, ImageDraw, ImageFont
import os

img_1 = Image.new('RGB', (100, 100), color='white')
draw = ImageDraw.Draw(img_1)
font = ImageFont.truetype('arial.ttf', 20)
width, height = img_1.size
draw.text((width / 2 - 3, height / 2 - 5), '1', fill='red')
draw.rectangle((0, 0, 100, 100), outline='blue', width=5)
img_1.show()

img_2 = Image.new('RGB', (100, 100), color='white')
draw = ImageDraw.Draw(img_2)
font2 = ImageFont.truetype('arial.ttf', 20)
draw.text((width / 2 - 3, height / 2 - 5), '2', fill='red')
draw.rectangle((0, 0, 100, 100), outline='blue', width=5)
img_2.show()

img_3 = Image.new('RGB', (100, 100), color='white')
draw = ImageDraw.Draw(img_3)
font3 = ImageFont.truetype('arial.ttf', 20)
draw.text((width / 2 - 3, height / 2 - 5), '3', fill='red')
draw.rectangle((0, 0, 100, 100), outline='blue', width=5)
img_3.show()

current_directory = os.path.dirname(os.path.abspath(__file__))
save_path1 = os.path.join(current_directory, "output_image_1.png")

img_1.save(save_path1)

save_path2 = os.path.join(current_directory, "output_image_2.png")

img_2.save(save_path2)

save_path3 = os.path.join(current_directory, "output_image_3.png")

img_3.save(save_path3)
