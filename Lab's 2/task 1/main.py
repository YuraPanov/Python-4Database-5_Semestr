from PIL import Image, ImageDraw, ImageFont

import sys

image_path = "test.jpg"
origin = Image.open(image_path)

origin.convert("RGB")
r, g, b = origin.split()

zero_channel = Image.new('L', origin.size)  # L (8-bit pixels, grayscale)
# Отдельно решил сделать грэйскейл
gray_image = origin.convert('L')
# Для визуализации каналов создадим новые изображения, где остальные каналы установлены в 0
r_image = Image.merge("RGB", (r, zero_channel, zero_channel))
g_image = Image.merge("RGB", (zero_channel, g, zero_channel))
b_image = Image.merge("RGB", (zero_channel, zero_channel, b))
# Считаем размеры исходника
width, height = origin.size
# Увеличиваем итоговый размер изображения до требуемого
combined_width = width * 5
combined_image = Image.new('RGB', (combined_width, height))
# Вставляем последовательно новые изображения
combined_image.paste(origin, (0, 0))
combined_image.paste(r_image, (width, 0))
combined_image.paste(g_image, (width * 2, 0))
combined_image.paste(b_image, (width * 3, 0))
combined_image.paste(gray_image, (width * 4, 0))

combined_image.show()
