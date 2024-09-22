import argparse
from pathlib import Path


def check_files_in_directory(dirpath, files_to_check):
    """Проверяет наличие файлов в указанной директории."""
    existing_files = []
    missing_files = []

    for file_name in files_to_check:
        file_path = dirpath / file_name
        if file_path.exists():
            existing_files.append(file_name)
        else:
            missing_files.append(file_name)

    return existing_files, missing_files


def write_results(dirpath, existing_files, missing_files):
    """Записывает результаты в текстовые файлы."""
    with open(dirpath / "existing_files.txt", "w") as f:
        f.write("\n".join(existing_files) + "\n")

    with open(dirpath / "missing_files.txt", "w") as n_f:
        n_f.write("\n".join(missing_files) + "\n")


def main():
    # Создаем парсер для аргументов
    parser = argparse.ArgumentParser(description="Проверка наличия файлов в папке.")
    parser.add_argument('--dirpath', type=str, default='.', help="Путь к папке (по умолчанию текущая папка).")
    parser.add_argument('--files', nargs='*', help="Список имен файлов для проверки.")

    # Парсим аргументы
    args = parser.parse_args()

    dirpath = Path(args.dirpath)

    # Проверяем, что папка существует
    if not dirpath.exists() or not dirpath.is_dir():
        print(f"Ошибка: папка {dirpath} не существует или не является директорией.")
        return

    # Проверяем наличие файлов
    if args.files:
        existing_files, missing_files = check_files_in_directory(dirpath, args.files)
    else:
        print("Ошибка: не указаны имена файлов для проверки.")
        return

    # Записываем результаты в файлы
    write_results(dirpath, existing_files, missing_files)

    # Выводим результат на экран
    print("Присутствуют файлы:")
    print("\n".join(existing_files) if existing_files else "Нет найденных файлов.")

    print("\nНе присутствуют файлы:")
    print("\n".join(missing_files) if missing_files else "Все файлы найдены.")


if __name__ == "__main__":
    main()
