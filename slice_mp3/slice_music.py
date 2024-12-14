from pydub import AudioSegment
import os

def split_mp3(input_file, output_folder, segment_length=20):
    """
    Разделяет MP3-файл на отрывки заданной длины.

    :param input_file: Путь к исходному MP3-файлу
    :param output_folder: Папка для сохранения отрывков
    :param segment_length: Длина отрывка в секундах (по умолчанию 20 секунд)
    """
    try:
        # Загружаем MP3-файл
        audio = AudioSegment.from_mp3(input_file)
        audio_length = len(audio)  # Длина аудио в миллисекундах

        # Проверяем, существует ли папка; если нет, то создаем
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Разбиваем аудио на части
        for i in range(0, audio_length, segment_length * 1000):  # 1 секунда = 1000 мс
            segment = audio[i:i + segment_length * 1000]
            segment_file = os.path.join(output_folder, f"segment_{i // 1000}-{(i + len(segment)) // 1000}.mp3")
            segment.export(segment_file, format="mp3")
            print(f"Сохранён отрывок: {segment_file}")

        print("Разбиение аудио завершено!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    # Указываем путь к входному MP3-файлу
    mp3_file = "C:/Users/Пользователь/PycharmProjects/ultima/res/music/sound_1.mp3"

    # Указываем папку, куда сохранять отрывки
    output_directory = "segments"

    # Указываем длину отрывка (в секундах)
    segment_duration = 20

    split_mp3(mp3_file, output_directory, segment_duration)
