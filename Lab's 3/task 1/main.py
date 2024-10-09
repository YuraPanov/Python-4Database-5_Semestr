from skimage import io, transform, color
from pathlib import Path
import argparse



def apply_augmentations(image, augmentations):
    for aug in augmentations:
        if aug == "rotate_90":
            image = transform.rotate(image, 90)
        elif aug == "rotate_45":
            image = transform.rotate(image, 45)
        elif aug == "resize":
            image = transform.resize(image, (100, 100))  # Пример изменения размера
        elif aug == "grayscale":
            image = color.rgb2gray(image)
        elif aug == "complex":
            image = transform.resize(transform.rotate(image, 45), (150, 150))  # Комплексное преобразование

    return image


parser = argparse.ArgumentParser()
parser.add_argument("-dir", required=True)
parser.add_argument("-augm", nargs="+", help="List: 1)rotate_90 2)rotate_45 3)resize 4)grayscale 5)complex")
args = parser.parse_args()

image_paths = list(Path(args.dir).glob('*'))

numberOf_file = 20

for img_path in image_paths[:numberOf_file]:
    try:
        # Читаем изображение
        img = io.imread(img_path)

        # Удаляем альфа-канал, если он есть
        if img.shape[2] == 4:  # Если изображение имеет 4 канала (RGBA)
            img = img[:, :, :3]  # Удаляем альфа-канал

        # Применяем аугментации
        augmented_img = apply_augmentations(img, args.augm)

        # Преобразуем изображение в правильный формат перед сохранением
        if augmented_img.dtype == 'float32' or augmented_img.dtype == 'float64':
            augmented_img = (augmented_img * 255).astype('uint8')  # Приведение к uint8

        # Определяем путь для сохранения
        save_path = Path(args.dir) / f"augmented_{img_path.name}"

        # Сохраняем обработанное изображение
        io.imsave(save_path, augmented_img)

        print(f"Обработано изображение: {img_path.name} -> {save_path.name}")
    except Exception as e:
        print(f"Ошибка при обработке {img_path.name}: {e}")
