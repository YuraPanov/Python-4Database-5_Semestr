import argparse
from pathlib import Path


def create_missing_files(dirpath, missing_files):
    """Создает отсутствующие файлы в указанной директории."""
    for file_name in missing_files:
        file_path = dirpath / file_name
        # Создаем пустой файл
        file_path.touch()
        print(f"Создан файл: {file_name}")


def read_missing_files(dirpath):
    """Читает список отсутствующих файлов из файла 'missing_files.txt'."""
    missing_files_file = dirpath / "missing_files.txt"

    if not missing_files_file.exists():
        print(f"Файл {missing_files_file} не найден.")
        return []

    with open(missing_files_file, "r") as f:
        return [line.strip() for line in f.readlines()]


def main():
    # Создаем парсер для аргументов
    parser = argparse.ArgumentParser(description="Создание отсутствующих файлов.")
    parser.add_argument('--dirpath', type=str, default='.', help="Путь к папке (по умолчанию текущая папка).")

    # Парсим аргументы
    args = parser.parse_args()
    dirpath = Path(args.dirpath)

    # Проверяем, что папка существует
    if not dirpath.exists() or not dirpath.is_dir():
        print(f"Ошибка: папка {dirpath} не существует или не является директорией.")
        return

    # Читаем отсутствующие файлы
    missing_files = read_missing_files(dirpath)

    if missing_files:
        create_missing_files(dirpath, missing_files)
    else:
        print("Нет отсутствующих файлов для создания.")


if __name__ == "__main__":
    main()
