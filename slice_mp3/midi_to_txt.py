from mido import MidiFile, bpm2tempo


# Функция перевода абсолютного времени (тики -> hh:mm:ss.mmm)
def convert_ticks_to_time(ticks, ticks_per_beat, tempo):
    seconds = (ticks / ticks_per_beat) * (tempo / 1_000_000)  # Перевод в секунды
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds_int = int(seconds % 60)  # Целая часть секунд
    milliseconds = int((seconds % 1) * 1000)  # Дробная часть (миллисекунды)
    return f"{hours:02}:{minutes:02}:{seconds_int:02}.{milliseconds:03}"


# Пути к файлам
midi_file_path = 'C:/Users/Пользователь/PycharmProjects/ultima/slice_mp3/result_file.mid'
output_file_path = 'C:/Users/Пользователь/PycharmProjects/ultima/slice_mp3/notes_output.txt'

# Открываем MIDI файл
mid = MidiFile(midi_file_path)

# Определяем темп (по умолчанию 120 BPM)
default_tempo = bpm2tempo(120)  # Стандартный темп: 120 ударов в минуту (в мкс)

# Перебираем все дорожки и формируем вывод
with open(output_file_path, 'w', encoding='utf-8') as file:
    for i, track in enumerate(mid.tracks):
        file.write(f"Track {i}: {track.name}\n")  # Имя дорожки
        absolute_ticks = 0  # Абсолютное время (тики)

        for msg in track:
            absolute_ticks += msg.time  # Суммируем время событий (в тиках)

            if msg.type == 'note_on' and msg.velocity > 0:
                # Конвертируем абсолютное время в формат hh:mm:ss.mmm
                time_formatted = convert_ticks_to_time(absolute_ticks, mid.ticks_per_beat, default_tempo)
                # Записываем в файл время, ноту и скорость
                file.write(f"Time: {time_formatted}, Note: {msg.note}, Velocity: {msg.velocity}\n")
