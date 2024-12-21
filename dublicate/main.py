import os
import shutil
from filecmp import cmp

# Пути к черновику и публичной папке
draft_folder = r"путь_к_черновику"  # Путь к черновику, например "C:/projects/draft"
public_folder = r"путь_к_публичной_папке"  # Путь к "публичной" папке, например "C:/projects/public"

# Разрешённые расширения (только .py и .txt)
allowed_extensions = {".py", ".txt"}


def find_unique_filename(directory, filename):
    """
    Генерирует уникальное имя файла, если файл с таким же названием уже существует в папке.
    Например: "file.py" -> "file (2).py" -> "file (3).py" и так далее.
    """
    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    # Ищем, пока не найдём уникальное название
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base_name} ({counter}){extension}"
        counter += 1

    return new_filename


def sync_directories(source, destination):
    """
    Синхронизирует файлы из source в destination.
    """
    for root, dirs, files in os.walk(source):
        # Сохраняем относительный путь текущей директории относительно source
        relative_path = os.path.relpath(root, source)
        destination_dir = os.path.join(destination, relative_path)

        # Создаём папки в публичной папке, если они отсутствуют
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Перебираем файлы в текущей директории
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[-1]

            # Проверяем, является ли файл разрешённым (.py или .txt)
            if file_extension in allowed_extensions:
                destination_file = os.path.join(destination_dir, file)

                # Если файла нет в публичной папке, копируем его
                if not os.path.exists(destination_file):
                    shutil.copy2(file_path, destination_file)
                    print(f"Скопирован: {file_path} -> {destination_file}")
                # Если файл есть, но содержимое разное, копируем с уникальным именем
                elif not cmp(file_path, destination_file, shallow=False):
                    unique_filename = find_unique_filename(destination_dir, file)
                    unique_destination_file = os.path.join(destination_dir, unique_filename)
                    shutil.copy2(file_path, unique_destination_file)
                    print(f"Файл отличается, скопирован с новым именем: {file_path} -> {unique_destination_file}")


if __name__ == "__main__":
    # Запуск синхронизации
    sync_directories(draft_folder, public_folder)
    print("Синхронизация завершена!")
