import matplotlib.pyplot as plt
from PIL import Image

image_path = "0210.jpg"
image = Image.open(image_path)
image = image.convert("RGB")
image.thumbnail((300, 300))
pixels = list(image.getdata())

r_value = [pixel[0] for pixel in pixels]
g_value = [pixel[1] for pixel in pixels]
b_value = [pixel[2] for pixel in pixels]

plt.figure(figsize=(10, 5))
plt.figure(figsize=(12, 12))
plt.tight_layout(pad=5.0)

plt.subplot(4, 2, (1,7))
plt.imshow(image)
plt.axis('off')

histogram = image.histogram()
plt.subplot(4, 2, 2)
plt.bar(range(256), histogram[:256], color='grey', width=1)
plt.bar(range(256), histogram[256:512], color='grey', width=1)
plt.bar(range(256), histogram[512:], color='grey', width=1)
plt.title('Гистограмма изображения')
plt.xlabel("Яркость")

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.subplot(4, 2, 4)
plt.hist(r_value, bins=256, color='red', alpha=0.7)
plt.title('Красный канал')
plt.xlabel("Яркость")
plt.subplot(4, 2, 6)
plt.hist(g_value, bins=256, color='green', alpha=0.7)
plt.title('Зелёный канал')
plt.xlabel("Яркость")
plt.subplot(4, 2, 8)
plt.hist(b_value, bins=256, color='blue', alpha=0.7)
plt.title('Синий канал')
plt.xlabel("Яркость")

plt.tight_layout()
plt.show()
