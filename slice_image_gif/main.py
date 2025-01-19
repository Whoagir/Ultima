from PIL import Image


def create_gif_frames(input_image_path, output_folder, frames_count):
    # Открываем изображение
    image = Image.open(input_image_path)
    width, height = image.size

    # Размеры каждого кадра (уменьшение в 4 раза)
    frame_width = width // 2
    frame_height = height // 3

    # Координаты начального и конечного положения
    start_x, start_y = 0, height - frame_height  # Левый нижний угол
    end_x, end_y = width - frame_width, 0  # Правый верхний угол

    # Шаги по осям
    step_x = (end_x - start_x) / (frames_count - 1)
    step_y = (end_y - start_y) / (frames_count - 1)

    # Генерация кадров
    for i in range(frames_count):
        # Рассчитываем текущие координаты
        current_x = int(start_x + step_x * i)
        current_y = int(start_y + step_y * i)

        # Обрезаем изображение
        frame = image.crop((current_x, current_y, current_x + frame_width, current_y + frame_height))

        # Сохраняем кадр
        frame.save(f"{output_folder}/frame_{i + 1:03d}.png")


# Пример использования
input_image_path = "snow2.png"  # Замените на ваш путь
output_folder = "frames"  # Папка для сохранения кадров
frames_count = 60

# Создайте папку для сохранения кадров (если нужно)
import os

os.makedirs(output_folder, exist_ok=True)

create_gif_frames(input_image_path, output_folder, frames_count)
