from pathlib import Path
import shutil


def main():
    # Получаем путь к текущему файлу и создаём папку для копирования
    current_file_path = Path(__file__)
    current_directory = current_file_path.parent
    target_folder = current_directory / 'example'
    small_folder = current_directory / 'small'
    small_folder.mkdir(exist_ok=True)

    max_size = 2048  # Максимальный размер файла в килобайтах
    matching_files = []

    Check_selFolder = input("Если хотите выбрать папку для сканирования, нажмите 1, если нет,\nто нажмите 2 чтобы была "
                            "использована папка по умолчанию.")
    try:
        if Check_selFolder == "1":
            target_folder = Path(input("Введите путь к папке: "))
            max_size = int(input("Введите максимальный размер файла в килобайтах: ")) * 1024  # Перевод в байты
            # Проверяем, что введённый путь существует и это папка
            if not target_folder.exists() or not target_folder.is_dir():
                raise FileNotFoundError("Путь не существует или не является директорией.")

            print(f"Выбрана папка: {target_folder.resolve()}")

        elif Check_selFolder == "2":
            print(f"Используем папку по умолчанию: {target_folder.resolve()}")

        else:
            raise ValueError("Неправильный ввод. Пожалуйста, введите 1 или 2.")

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return

    # Сканируем выбранную папку на наличие файлов
    for file in target_folder.iterdir():
        if file.is_file():
            file_size = file.stat().st_size
            if file_size < max_size:
                matching_files.append(file)

    # Выводим подходящие файлы и копируем их
    print("Подходящие файлы:")
    for file in matching_files:
        print(f"{file.name}")

    for file in matching_files:
        destination = small_folder / file.name
        shutil.copy(file, destination)
        print(f"Скопирован файл: {file.name} в папку 'small'")


if __name__ == "__main__":
    main()
