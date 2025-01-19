import ffmpeg
import os

def remove_static_scenes_with_mpdecimate(input_file, output_file):
    """
    Удаляет статичные сцены из видео с помощью фильтра mpdecimate.

    :param input_file: Путь к входному видеофайлу.
    :param output_file: Путь к выходному видеофайлу.
    """
    try:
        # Проверяем, существует ли входной файл
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Файл {input_file} не найден.")

        # Используем ffmpeg с фильтром mpdecimate
        (
            ffmpeg
            .input(input_file)
            .filter('mpdecimate')  # Удаляем дублирующиеся кадры
            .filter('setpts', 'N/FRAME_RATE/TB')  # Исправляем временные метки
            .output(output_file)
            .run(overwrite_output=True)
        )

        print(f"Обработка завершена. Результат сохранен в {output_file}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
input_video = "res/3.mp4"  # Укажите путь к вашему видео
output_video = "res/output3.mp4"  # Укажите путь для сохранения результата
remove_static_scenes_with_mpdecimate(input_video, output_video)