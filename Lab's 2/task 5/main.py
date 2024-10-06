from PIL import Image
import os


def show_sketches(extension):
    # Получаем список всех файлов с заданным расширением в текущей директории
    files = [f for f in os.listdir() if f.endswith(extension)]

    if not files:
        print(f"Нет файлов с расширением {extension} в текущей папке.")
        return

    # Для каждого файла создаем и показываем эскиз
    for file in files:
        try:
            # Открываем изображение
            img = Image.open(file)

            # Создаем эскиз (thumbnail) размером 50x50
            img.thumbnail((50, 50))

            # Показываем изображение
            img.show()

        except Exception as e:
            print(f"Ошибка при обработке файла {file}: {e}")


file_type = input("Введите расширение файлов для просмотра (например, '.jpg', '.png'): ")
show_sketches(file_type)
