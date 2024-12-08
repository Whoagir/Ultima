import os

# Путь до директории, где будем искать
directory = 'D:\\'
# Файл, куда будем сохранять пути к найденным файлам
output_file = 'path.txt'

n = 0
# Открываем файл для записи
with open(output_file, 'w', encoding='utf-8') as output:
    # Проходим по всем подкаталогам и файлам в указанной директории
    for subdir, _, files in os.walk(directory):
        for file in files:
            # Проверяем имеет ли файл расширение .txt
            if file.endswith('.txt'):
                file_path = os.path.join(subdir, file)
                try:
                    # Открываем файл и читаем его содержимое
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        n += 1
                        # Проверяем наличие словосочетания "алгоритм дейкстры" в любом регистре
                        if "алгоритм дейкстры" in content.lower():
                            # Записываем путь к файлу в output.txt
                            output.write(str(n) + ". " +  file_path + '\n')
                except Exception as e:
                    n += 1
                    # Выводим ошибку, если файл не может быть прочитан
                    print(f"{n}.Не удалось прочитать файл {file_path}: {e}")

print("Поиск завершен. Пути к файлам сохранены в path.txt.")
